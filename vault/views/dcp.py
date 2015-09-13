from django.core.urlresolvers import reverse_lazy
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from cinesend.utils import LoginRequiredMixin
from vault.models.dcp import DCP


def get_dcp_or_404(slug, user):
    dcp = get_object_or_404(DCP, slug=slug)
    if (dcp.asset.made_by != user and user not in dcp.asset.owners.all()) or (
            dcp.job.made_by != user and user not in dcp.job.owners.all()):
        raise Http404
    return dcp


class DCPDetailView(LoginRequiredMixin, DetailView):
    template_name = 'vault/dcp/dcp-detail.html'
    context_object_name = 'dcp'

    def get_object(self, queryset=None):
        return get_dcp_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)


class DCPDeleteView(LoginRequiredMixin, DeleteView):
    model = DCP
    template_name = 'vault/dcp/dcp-delete.html'
    context_object_name = 'dcp'

    def get_object(self, queryset=None):
        return get_dcp_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_success_url(self):
        asset = self.object.asset
        return reverse_lazy('asset-detail', kwargs={'slug': asset.slug})