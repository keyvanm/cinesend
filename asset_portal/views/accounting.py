from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django_tables2 import RequestConfig
from django.db.models import Q
import stripe

from user_manager.models.accounting import Invoice
from user_manager.models.user_profile import CreditCard
from asset_portal.views import get_job_or_404
from cinesend.utils import LoginRequiredMixin
from asset_portal.models import Job
from asset_portal.tables import JobInvoiceTable


class JobPayListView(LoginRequiredMixin, View):
    def get(self, request):
        jobs = Job.objects.select_subclasses().filter(
            Q(canceled=False) & (Q(made_by=request.user) | Q(owners=request.user)) & Q(paid=False) & Q(
                fee__gt=0)).distinct()
        jobs_table = JobInvoiceTable(jobs)
        RequestConfig(request, paginate=False).configure(jobs_table)
        return render(request, 'asset_portal/accounting/job-list-accounting.html',
                      {'jobs_table': jobs_table, 'jobs_len': jobs.count()})


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def create_and_charge_new_customer(jobs_to_pay_list, request, token, total_price):
    request.user.creditcards.all().delete()
    customer = stripe.Customer.create(
        source=token,
        description="{}, customer of {}".format(request.user.get_full_name(),
                                                get_current_site(request).name),
        email=request.user.email
    )
    request.user.profile.stripe_customer_id = customer.stripe_id
    request.user.profile.save()
    stripe.Charge.create(
        amount=int(total_price * 100),  # amount in cents, again
        currency="cad",
        customer=customer.id,
        description="Paid ${} for jobs {}".format(total_price,
                                                  " ".join([job.slug for job in jobs_to_pay_list]))
    )


def get_jobs_to_pay_list(jobs_to_pay_slug_list, user):
    jobs_to_pay_list = []
    for slug in jobs_to_pay_slug_list:
        job = get_job_or_404(slug, user)
        if not job.paid and job.fee > 0:
            jobs_to_pay_list.append(job)
    return jobs_to_pay_list


class JobCartView(LoginRequiredMixin, View):
    def get(self, request):
        jobs_to_pay_slug_list = request.GET.getlist("pay")
        jobs_to_pay_list = get_jobs_to_pay_list(jobs_to_pay_slug_list, request.user)
        total_price_before_tax = Decimal(0)
        for job in jobs_to_pay_list:
            total_price_before_tax += job.fee

        if not jobs_to_pay_list or total_price_before_tax == 0:
            messages.warning(request, 'All items in your cart are already paid for.')
            raise Http404

        total_price = (total_price_before_tax * Decimal("1.13")).quantize(Decimal("1.00"))
        total_tax = (total_price_before_tax * Decimal("0.13")).quantize(Decimal("1.00"))

        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        return render(request, 'asset_portal/accounting/cart.html',
                      {'jobs': jobs_to_pay_list, 'total_price': total_price, 'stripe_public_key': stripe_public_key,
                       'total_price_before_tax': total_price_before_tax, 'total_tax': total_tax,
                       'total_price_cents': int(total_price * 100)})

    @method_decorator(csrf_protect)
    def post(self, request):
        jobs_to_pay_slug_list = request.POST.getlist("pay")
        jobs_to_pay_list = get_jobs_to_pay_list(jobs_to_pay_slug_list, request.user)
        total_price = Decimal(0)
        for job in jobs_to_pay_list:
            total_price += job.fee
        total_price *= Decimal("1.13")

        if not jobs_to_pay_list or total_price == 0:
            messages.warning(request, 'All items in your cart are already paid for.')
            raise Http404
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        token = request.POST['stripeToken']
        try:
            if not request.user.profile.stripe_customer_id:
                create_and_charge_new_customer(jobs_to_pay_list, request, token, total_price)
            else:
                customer = stripe.Customer.retrieve(request.user.profile.stripe_customer_id)
                if customer.get("deleted", None):
                    create_and_charge_new_customer(jobs_to_pay_list, request, token, total_price)
                else:
                    token_object = stripe.Token.retrieve(token)
                    cc = get_or_none(CreditCard, user=request.user, fingerprint=token_object.card.fingerprint)
                    if cc is None:
                        card = customer.sources.create(source=token)
                        cc = CreditCard(user=request.user, fingerprint=card.fingerprint, card_id=card.id)
                        cc.save()
                    stripe.Charge.create(
                        amount=int(total_price * 100),  # amount in cents, again
                        currency="cad",
                        source=cc.card_id,
                        customer=customer.id,
                        description="Paid ${} for jobs {}".format(total_price,
                                                                  " ".join([job.slug for job in jobs_to_pay_list]))
                    )
            invoice = Invoice(paid_by=request.user)
            invoice.save()
            for job in jobs_to_pay_list:
                job.invoice = invoice
                job.paid = True
                job.save(update_fields=("invoice", "paid",))
            messages.success(request, 'Transaction successful')
            return redirect('accounting-home')
        except stripe.CardError, e:
            # The card has been declined
            messages.warning(request, 'Transaction unsuccessful. Please try again.')
            return render(request, 'asset_portal/accounting/cart.html',
                          {'jobs': jobs_to_pay_list, 'total_price': total_price,
                           'stripe_public_key': stripe_public_key})

