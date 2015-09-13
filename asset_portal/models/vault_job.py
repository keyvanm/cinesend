from django.db import models
from django.db.models.signals import post_save
from asset_portal.models import Job
from asset_portal.models.job import EncodeDVDJob, EncodeBlurayJob
from user_manager.models import Address
from vault.models.optical_disc import DVD, Bluray

__author__ = 'k1'


class SendDVDJob(Job):
    dvd = models.ForeignKey(DVD)

    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Requested'),
        (33, 'In Progress'),
        (66, 'Shipped'),
        (100, 'Received'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    addresses = models.ManyToManyField(Address)
    type = "Send DVD"

    def get_price(self):
        return 7


# automatically make a dvd when an EncodeDVDJob is requested
def create_dvd(sender, **kwargs):
    created = kwargs["created"]
    if created:
        job = kwargs["instance"]
        if not DVD.objects.filter(job=job):
            dvd = DVD(job=job)
            dvd.asset = job.asset
            dvd.title = dvd.asset.film_title + ' DVD'
            dvd.running_time = 0
            dvd.region = job.video_format
            dvd.save()
post_save.connect(create_dvd, sender=EncodeDVDJob)

class SendBlurayJob(Job):
    bluray = models.ForeignKey(Bluray)

    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Requested'),
        (33, 'In Progress'),
        (66, 'Shipped'),
        (100, 'Received'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    addresses = models.ManyToManyField(Address)
    type = "Send Bluray"

    def get_price(self):
        return 15

# automatically make a dvd when an EncodeDVDJob is requested
def create_bluray(sender, **kwargs):
    created = kwargs["created"]
    if created:
        job = kwargs["instance"]
        if not Bluray.objects.filter(job=job):
            bluray = Bluray(job=job)
            bluray.asset = job.asset
            bluray.title = bluray.asset.film_title + ' Bluray'
            bluray.running_time = 0
            bluray.save()
post_save.connect(create_bluray, sender=EncodeBlurayJob)