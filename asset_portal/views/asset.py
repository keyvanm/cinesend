from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django_tables2 import RequestConfig
from django.db.models import Q

from asset_portal.models import Asset, Job
from asset_portal.models.flight import Flight
from asset_portal.tables import AssetTable
from cinesend.utils import LoginRequiredMixin, grouper
from asset_portal.forms import AssetForm
from vault.models.dcp import DCP
from vault.models.optical_disc import DVD, Bluray


def is_a_dcp_made(asset_jobs):
    for job in asset_jobs:
        if job.type == "Make DCP":
            return True
    return False


class AssetListView(LoginRequiredMixin, View):
    def get(self, request):
        assets_table = AssetTable(Asset.objects.filter(
            Q(deleted=False) & (Q(made_by=request.user) | Q(owners=request.user))
        ).distinct())
        RequestConfig(request, paginate=False).configure(assets_table)
        return render(request, 'asset_portal/asset/asset-list.html', {'assets_table': assets_table})


class AssetTrackingView(LoginRequiredMixin, DetailView):
    template_name = 'asset_portal/asset/asset-tracking.html'
    context_object_name = 'asset'

    def get_object(self, queryset=None):
        return get_asset_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)


class AssetDetailView(LoginRequiredMixin, DetailView):
    template_name = 'asset_portal/asset/asset-detail.html'
    context_object_name = 'asset'

    def get_object(self, queryset=None):
        return get_asset_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AssetDetailView, self).get_context_data(**kwargs)
        asset = self.object
        jobs = Job.objects.select_subclasses().filter(
            Q(asset=asset) & Q(canceled=False) & (Q(made_by=self.request.user) | Q(owners=self.request.user))
        ).distinct()
        flights = Flight.objects.filter(job__asset=asset)

        dcps = DCP.objects.filter(
            Q(asset=asset) & (Q(job__made_by=self.request.user) | Q(job__owners=self.request.user)))
        disable_send_dcp = len(dcps) == 0
        dcps = grouper(dcps, 6)

        dvds = grouper(DVD.objects.filter(asset=asset), 6)
        blurays = grouper(Bluray.objects.filter(asset=asset), 6)

        context.update({'jobs': jobs, 'flights': flights, 'dcps': dcps, 'dvds': dvds, 'blurays': blurays,
                        'disable_send_dcp': disable_send_dcp})
        return context


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'asset_portal/asset/asset-create.html'

    def get_success_url(self):
        return reverse('asset-tracking', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        messages.success(self.request, 'Asset {0} created successfully'.format(form.instance.film_title))
        return super(AssetCreateView, self).form_valid(form)


class AssetEditView(LoginRequiredMixin, UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = 'asset_portal/asset/asset-edit.html'

    def get_object(self, queryset=None):
        asset = get_asset_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)
        if asset.status == 100:
            raise Http404
        return asset

    def form_valid(self, form):
        messages.success(self.request, 'Asset {0} edited successfully'.format(form.instance.film_title))
        return super(AssetEditView, self).form_valid(form)


class AssetDeleteView(LoginRequiredMixin, View):
    def get(self, request, slug):
        asset = get_asset_or_404(slug, request.user)
        jobs = Job.objects.select_subclasses().filter(
            Q(asset=asset) & Q(canceled=False) & (Q(made_by=request.user) | Q(owners=request.user))
        ).distinct()
        return render(request, 'asset_portal/asset/asset-delete.html', {'asset': asset, "jobs": jobs})

    def post(self, request, slug):
        asset = get_asset_or_404(slug, request.user)
        if asset.job_set.all():
            messages.error(request,
                           'Asset {0} can\'t be deleted due to outstanding active jobs'.format(asset.film_title))
            return redirect('asset-list')
        asset.deleted = True
        asset.save(update_fields=('deleted',))
        messages.success(request, 'Asset {0} deleted successfully'.format(asset.film_title))
        return redirect('asset-list')


def get_asset_or_404(slug, user):
    asset = get_object_or_404(Asset, slug=slug)
    if (asset.made_by != user and user not in asset.owners.all()) or asset.deleted:
        raise Http404
    return asset
