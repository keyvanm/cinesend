from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.detail import DetailView
from django_tables2 import RequestConfig
from django.db.models import Q

from asset_portal.models import Flight
from asset_portal.tables import FlightTable
from cinesend.utils import LoginRequiredMixin


def get_flight_or_404(pk, user):
    flight = get_object_or_404(Flight, pk=pk)
    if not flight.job or (flight.job.made_by != user and user not in flight.job.owners.all()) or flight.job.canceled:
        raise Http404
    return flight


class FlightListView(LoginRequiredMixin, View):
    def get(self, request):
        flights_table = FlightTable(Flight.objects.filter(
            Q(job__canceled=False) & (Q(job__made_by=request.user) | Q(job__owners=request.user))
        ).distinct())
        RequestConfig(request, paginate=False).configure(flights_table)
        return render(request, 'asset_portal/flight/flight-list.html', {'flights_table': flights_table})


class FlightDetailView(LoginRequiredMixin, DetailView):
    template_name = 'asset_portal/flight/flight-detail.html'
    context_object_name = 'flight'

    def get_object(self, queryset=None):
        return get_flight_or_404(self.kwargs[self.pk_url_kwarg], self.request.user)
