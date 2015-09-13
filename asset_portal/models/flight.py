from django.db.models.signals import m2m_changed
# from django.contrib import messages
from django.db import models
from job import SendDCPJob
from user_manager.models.exhibitor import ScreeningRoom


class Flight(models.Model):
    job = models.ForeignKey(SendDCPJob)
    screening_room = models.ForeignKey(ScreeningRoom)
    STATUS_CHOICES = (
        (1, 'In Progress'),
        (100, 'Complete'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)


def create_flights(sender, **kwargs):
    """When creating a new SendDCPJob, make the flights for it."""
    job = kwargs["instance"]
    for addr in job.addresses.all():
        if not Flight.objects.filter(job=job, screening_room=addr):
            flight = Flight(job=job, screening_room=addr)
            # messages.success(request, 'Flight {0} created successfully'.format(flight))
            flight.save()


m2m_changed.connect(create_flights, sender=SendDCPJob.addresses.through)
