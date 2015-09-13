from django.core.urlresolvers import reverse_lazy
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from cinesend.utils import LoginRequiredMixin
from vault.models.optical_disc import DVD, Bluray


def get_dvd_or_404(slug, user):
    dvd = get_object_or_404(DVD, slug=slug)
    if (dvd.asset.made_by != user and user not in dvd.asset.owners.all()):
        raise Http404
    return dvd


def get_bluray_or_404(slug, user):
    bluray = get_object_or_404(Bluray, slug=slug)
    if (bluray.asset.made_by != user and user not in bluray.asset.owners.all()):
        raise Http404
    return bluray


class DVDDetailView(LoginRequiredMixin, DetailView):
    model = DVD
    template_name = 'vault/optical_disc/dvd-detail.html'
    context_object_name = 'disc'

    def get_object(self, queryset=None):
        return get_dvd_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)


class DVDDeleteView(LoginRequiredMixin, DeleteView):
    model = DVD
    template_name = 'vault/optical_disc/dvd-delete.html'
    context_object_name = 'disc'

    def get_object(self, queryset=None):
        return get_dvd_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_success_url(self):
        asset = self.object.asset
        return reverse_lazy('asset-detail', kwargs={'slug': asset.slug})


class BlurayDetailView(LoginRequiredMixin, DetailView):
    model = Bluray
    template_name = 'vault/optical_disc/bluray-detail.html'
    context_object_name = 'disc'

    def get_object(self, queryset=None):
        return get_bluray_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)


class BlurayDeleteView(LoginRequiredMixin, DeleteView):
    model = Bluray
    template_name = 'vault/optical_disc/bluray-delete.html'
    context_object_name = 'disc'

    def get_object(self, queryset=None):
        return get_bluray_or_404(self.kwargs[self.slug_url_kwarg], self.request.user)

    def get_success_url(self):
        asset = self.object.asset
        return reverse_lazy('asset-detail', kwargs={'slug': asset.slug})