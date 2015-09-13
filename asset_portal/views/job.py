from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import View
from django.db.models import Q
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import RequestConfig

from asset_portal.models import Job
import asset_portal.models as apm
from asset_portal.models.job import MakeDCPJob, RequestQCCheckJob, OrderPhysicalDCPJob, SendDCPJob, EncodeDVDJob, \
    EncodeBlurayJob
from asset_portal.models.vault_job import SendBlurayJob, SendDVDJob
from asset_portal.tables import JobTable
from user_manager.models.address import Address
from cinesend.utils import LoginRequiredMixin
from asset_portal.forms import RequestQCCheckJobForm, OrderPhysicalDCPJobForm, \
    MakeDCPJobForm, SendDCPJobForm, SendDVDJobForm, SendBlurayJobForm, EncodeDVDJobForm, EncodeBlurayJobForm
from asset_portal.views import get_asset_or_404, is_a_dcp_made
from vault.views.optical_disc import get_dvd_or_404, get_bluray_or_404


def get_job_or_404(slug, user):
    job = Job.objects.get_subclass(slug=slug)
    if not job or (job.made_by != user and user not in job.owners.all()) or job.canceled:
        raise Http404
    return job


class JobListView(LoginRequiredMixin, View):
    def get(self, request):
        jobs_table = JobTable(Job.objects.select_subclasses().filter(
            Q(canceled=False) & (Q(made_by=request.user) | Q(owners=request.user))
        ).distinct())
        RequestConfig(request, paginate=False).configure(jobs_table)
        return render(request, 'asset_portal/job/job-list.html', {'jobs_table': jobs_table})


class JobDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'job'

    def get_object(self, queryset=None):
        return get_job_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_template_names(self):
        job = self.object
        if isinstance(job, apm.RequestQCCheckJob):
            return 'asset_portal/job/job-detail-requestqcjob.html'
        elif isinstance(job, apm.OrderPhysicalDCPJob):
            return 'asset_portal/job/job-detail-orderphysicaldcp.html'
        elif isinstance(job, apm.MakeDCPJob):
            return 'asset_portal/job/job-detail-makedcpjob.html'
        elif isinstance(job, apm.SendDCPJob):
            return 'asset_portal/job/job-detail-senddcpjob.html'
        elif isinstance(job, SendDVDJob):
            return 'asset_portal/job/job-detail-senddvdjob.html'
        elif isinstance(job, SendBlurayJob):
            return 'asset_portal/job/job-detail-sendblurayjob.html'
        elif isinstance(job, apm.EncodeDVDJob):
            return 'asset_portal/job/job-detail-encodedvdjob.html'
        elif isinstance(job, apm.EncodeBlurayJob):
            return 'asset_portal/job/job-detail-encodeblurayjob.html'
        elif isinstance(job, apm.ShippingJob):
            return 'asset_portal/job/job-detail-shippingjob.html'
        # if isinstance(job, apm.RequestLogoChangeJob):
        # return 'asset_portal/job/job-detail-requestlogochangejob.html'
        else:
            return 'asset_portal/job/job-detail.html'


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = None
    template_name = 'asset_portal/job/job-create.html'


    def get_success_url(self):
        return reverse('job-detail', kwargs={'slug': self.object.slug})

    def get_asset(self):
        return get_asset_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_context_data(self, **kwargs):
        context = super(JobCreateView, self).get_context_data(**kwargs)
        asset = self.get_asset()
        price = self.model(asset=asset).get_price()
        context.update({'asset': asset, 'price': price})
        return context

    def process_fee(self, form):
        return form.instance.get_price()

    def form_valid(self, form):
        asset = self.get_asset()
        form.instance.made_by = self.request.user
        form.instance.asset = asset
        form.instance.fee = self.process_fee(form)
        if form.instance.fee == 0:
            form.instance.paid = True
        messages.success(self.request, 'Job {0} created successfully.'.format(form.instance.type) +
                         ' Remember, you must pay for your jobs before they are started.')
        return super(JobCreateView, self).form_valid(form)


# class JobCreateLogoChangeView(JobCreateView):
# model = RequestLogoChangeJob
# form_class = RequestLogoChangeJobForm
#
# def get_context_data(self, **kwargs):
# context = super(JobCreateLogoChangeView, self).get_context_data(**kwargs)
# asset = context['asset']
# if asset.content_type != "FTR":
# raise Http404
# return context


class JobCreateQualityCheckView(JobCreateView):
    model = RequestQCCheckJob
    form_class = RequestQCCheckJobForm


class JobCreatePhysicalDCPView(JobCreateView):
    model = OrderPhysicalDCPJob
    form_class = OrderPhysicalDCPJobForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.profile.org or request.user.profile.org.type != "RESELLER":
            raise Http404
        return super(JobCreatePhysicalDCPView, self).dispatch(request, args, kwargs)


class JobCreateMakeDCPView(JobCreateView):
    model = MakeDCPJob
    form_class = MakeDCPJobForm
    template_name = 'asset_portal/job/job-create-makedcp.html'

    def process_fee(self, form):
        price, extra_price = form.instance.get_price()
        return price + (form.instance.number_of_copies - 1) * extra_price

    def get_context_data(self, **kwargs):
        context = super(JobCreateMakeDCPView, self).get_context_data(**kwargs)
        asset = context['asset']
        price, extra_price = self.model(asset=asset).get_price()
        context.update({'price': price, 'extra_price': extra_price})
        return context


class JobCreateSendDCPView(JobCreateView):
    model = SendDCPJob
    form_class = SendDCPJobForm

    def get_context_data(self, **kwargs):
        context = super(JobCreateSendDCPView, self).get_context_data(**kwargs)
        asset = context['asset']
        jobs = Job.objects.select_subclasses().filter(
            Q(asset=asset) & Q(canceled=False) & (Q(made_by=self.request.user) | Q(owners=self.request.user))
        ).distinct()
        if not is_a_dcp_made(jobs):
            raise Http404
        return context


class JobCreateEncodeDVDView(JobCreateView):
    model = EncodeDVDJob
    form_class = EncodeDVDJobForm


class JobCreateSendDVDView(JobCreateView):
    model = SendDVDJob
    form_class = SendDVDJobForm
    template_name = 'asset_portal/job/job-create-senddisc.html'

    def get_dvd(self):
        return get_dvd_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_asset(self):
        dvd = self.get_dvd()
        return dvd.asset

    def get_form(self, form_class):
        form = super(JobCreateSendDVDView, self).get_form(form_class)
        form.fields['addresses'].queryset = Address.objects.filter(user=self.request.user, type='shipping',
                                                                   privacy='private')
        return form

    def process_fee(self, form):
        return form.fields['addresses'].queryset.count() * form.instance.get_price()

    def form_valid(self, form):
        dvd = self.get_dvd()
        form.instance.dvd = dvd
        return super(JobCreateSendDVDView, self).form_valid(form)


class JobCreateEncodeBlurayView(JobCreateView):
    model = EncodeBlurayJob
    form_class = EncodeBlurayJobForm


class JobCreateSendBlurayView(JobCreateView):
    model = SendBlurayJob
    form_class = SendBlurayJobForm
    template_name = 'asset_portal/job/job-create-senddisc.html'

    def get_bluray(self):
        return get_bluray_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_asset(self):
        bluray = self.get_bluray()
        return bluray.asset

    def get_form(self, form_class):
        form = super(JobCreateSendBlurayView, self).get_form(form_class)
        form.fields['addresses'].queryset = Address.objects.filter(user=self.request.user, type='shipping',
                                                                   privacy='private')
        return form

    def process_fee(self, form):
        return form.fields['addresses'].queryset.count() * form.instance.get_price()

    def form_valid(self, form):
        bluray = self.get_bluray()
        form.instance.bluray = bluray
        return super(JobCreateSendBlurayView, self).form_valid(form)


class JobEditView(LoginRequiredMixin, UpdateView):
    template_name = 'asset_portal/job/job-edit.html'

    def get_object(self, queryset=None):
        job = get_job_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)
        if job.paid:
            messages.error(self.request, "You cannot edit a job that has already been paid for.")
            raise Http404
        self.model = job.__class__
        return job

    # def get_template_names(self):
    # job = self.object
    # if isinstance(job, apm.RequestLogoChangeJob):
    # return 'asset_portal/job/job-edit-requestlogochangejob.html'
    #     elif isinstance(job, apm.RequestQCCheckJob):
    #         return 'asset_portal/job/job-edit-requestqcjob.html'
    #     elif isinstance(job, apm.OrderPhysicalDCPJob):
    #         return 'asset_portal/job/job-edit-orderphysicaldcp.html'
    #     elif isinstance(job, apm.MakeDCPJob):
    #         return 'asset_portal/job/job-edit-makedcpjob.html'
    #     elif isinstance(job, apm.SendDCPJob):
    #         return 'asset_portal/job/job-edit-senddcpjob.html'
    #     elif isinstance(job, apm.SendDVDJob):
    #         return 'asset_portal/job/job-edit-senddvdjob.html'
    #     elif isinstance(job, apm.SendBlurayJob):
    #         return 'asset_portal/job/job-edit-sendblurayjob.html'
    #     elif isinstance(job, apm.ShippingJob):
    #         return 'asset_portal/job/job-edit-shippingjob.html'
    #     else:
    #         return 'asset_portal/job/job-edit.html'

    def get_form_class(self):
        job = self.object
        if isinstance(job, apm.RequestQCCheckJob):
            return RequestQCCheckJobForm
        elif isinstance(job, apm.OrderPhysicalDCPJob):
            return OrderPhysicalDCPJobForm
        elif isinstance(job, apm.MakeDCPJob):
            return MakeDCPJobForm
        elif isinstance(job, apm.SendDCPJob):
            return SendDCPJobForm
        elif isinstance(job, SendDVDJob):
            return SendDVDJobForm
        elif isinstance(job, SendBlurayJob):
            return SendBlurayJobForm
        # elif isinstance(job, apm.RequestLogoChangeJob):
        #     return RequestLogoChangeJobForm
        else:
            raise Http404

    def process_fee(self, form):
        if form.instance.type == "Make DCP":
            price, extra_price = form.instance.get_price()
            return price + (form.instance.number_of_copies - 1) * extra_price
        return form.instance.fee

    def form_valid(self, form):
        form.instance.fee = self.process_fee(form)
        if form.instance.fee == 0:
            form.instance.paid = True
        messages.success(self.request, 'Job {0} edited successfully'.format(form.instance.type))
        return super(JobEditView, self).form_valid(form)


class JobDeleteView(LoginRequiredMixin, View):
    def get(self, request, slug):
        job = get_job_or_404(slug, request.user)
        if job.type == "Shipping" or job.paid:
            messages.error(self.request, "You cannot delete a job that is already been paid for.")
            raise Http404
        return render(request, 'asset_portal/job/job-delete.html', {'job': job})

    def post(self, request, slug):
        job = get_job_or_404(slug, request.user)
        if job.type == "Shipping" or job.paid:
            messages.error(self.request, "You cannot delete a job that is already been paid for.")
            raise Http404
        job.canceled = True
        job.save(update_fields=('canceled',))
        messages.success(request, 'Job {0} deleted successfully'.format(job.type))
        return redirect('job-list')
