from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager
from model_utils.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from asset import Asset
from user_manager.models.exhibitor import ScreeningRoom
from user_manager.models.accounting import Invoice


class Job(TimeStampedModel):
    made_by = models.ForeignKey(User, related_name='+')
    owners = models.ManyToManyField(User, null=True, blank=True, related_name='+')
    asset = models.ForeignKey(Asset)
    type = "Generic Job"
    slug = AutoSlugField(populate_from=('asset', 'type', 'created'), unique=True)

    paid = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    fee = models.DecimalField(max_digits=20, decimal_places=2)
    invoice = models.ForeignKey(Invoice, null=True, blank=True)
    notes = models.TextField(blank=True)
    objects = InheritanceManager()

    @property
    def deleted(self):
        return self.canceled

    def __unicode__(self):
        return u'%s - %s (%s)' % (self.type, self.asset.film_title, self.created.date())

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})

    def get_price(self):
        return 0, 0


class ShippingJob(Job):
    STATUS_CHOICES = (
        (0, 'Canceled'),
        (1, 'Entered'),
        (50, 'In Transit'),
        (100, 'Delivered'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    fedex_tracking = models.CharField(max_length=20)
    type = "Shipping"


#
# class RequestLogoChangeJob(Job):
# # made_by = models.ForeignKey(User, related_name='rlc_jobs_created')
# # owners = models.ManyToManyField(User, null=True, blank=True, related_name='rlc_jobs_owned')
#
# STATUS_CHOICES = (
#         (0, 'Error'),
#         (1, 'Requested'),
#         (20, 'Awaiting Content'),
#         (40, 'Received'),
#         (60, 'Pending Review'),
#         (80, 'In Progress'),
#         (100, 'Completed'),
#     )
#     status = models.IntegerField(choices=STATUS_CHOICES, default=1)
#
#     version_name = models.CharField(max_length=200)
#     logos = models.ManyToManyField(Logo, related_name='parent_job')
#     type = "Request Logo Change"


class RequestQCCheckJob(Job):
    # made_by = models.ForeignKey(User, related_name='rqcc_jobs_created')
    # owners = models.ManyToManyField(User, null=True, blank=True, related_name='rqcc_jobs_owned')
    STATUS_CHOICES = (
        (0, 'Fail'),
        (1, 'Requested'),
        (33, 'Scheduled'),
        (66, 'In Progress'),
        (100, 'Pass'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    type = "Request Quality Check"


class OrderPhysicalDCPJob(Job):
    # made_by = models.ForeignKey(User, related_name='opdcp_jobs_created')
    # owners = models.ManyToManyField(User, null=True, blank=True, related_name='opdcp_jobs_owned')
    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Requested'),
        (33, 'In Progress'),
        (66, 'Shipped'),
        (100, 'Received'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    two_d_to_3d = models.BooleanField(default=False, verbose_name='Make 2D version from 3D source')
    four_k_to_2K_scaling = models.BooleanField(default=False, verbose_name='Make 2D version from 4K source')
    foureight_fps_to_twofour_fps = models.BooleanField(default=False,
                                                       verbose_name='Make 24 fps version from HFR source')
    audio_adjustment_to_85dBs = models.BooleanField(default=False, verbose_name='Adjust loudness to 85Leq(M)')

    create_encrypted_dcp = models.BooleanField(default=False, verbose_name='Create Encrypted DCP')

    COPIES_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    number_of_copies = models.IntegerField(choices=COPIES_CHOICES, default=1)
    type = "Order Physical DCP"


class MakeDCPJob(Job):
    # made_by = models.ForeignKey(User, related_name='mkdcp_jobs_created')
    # owners = models.ManyToManyField(User, null=True, blank=True, related_name='mkdcp_jobs_owned')
    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Requested'),
        (50, 'In Progress'),
        (100, 'Completed'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    two_d_to_3d = models.BooleanField(default=False, verbose_name='Make 2D version from 3D source')
    four_k_to_2K_scaling = models.BooleanField(default=False, verbose_name='Make 2D version from 4K source')
    foureight_fps_to_twofour_fps = models.BooleanField(default=False,
                                                       verbose_name='Make 24 fps version from HFR source')
    audio_adjustment_to_85dBs = models.BooleanField(default=False, verbose_name='Adjust loudness to 85Leq(M)')
    COPIES_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    number_of_copies = models.IntegerField(choices=COPIES_CHOICES, default=1)

    create_encrypted_dcp = models.BooleanField(default=False, verbose_name='Create Encrypted DCP')
    type = "Make DCP"

    def get_price(self):
        if self.asset.content_type == "FTR":
            price = 775
            extra_price = 225
        elif self.asset.content_type == "SHR30":
            price = 175
            extra_price = 75
        else:
            price = 105
            extra_price = 45
        return price, extra_price


class SendDCPJob(Job):
    # made_by = models.ForeignKey(User, related_name='senddcp_jobs_created')
    # owners = models.ManyToManyField(User, null=True, blank=True, related_name='senddcp_jobs_owned')
    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Requested'),
        (50, 'In Progress'),
        (100, 'Completed'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    addresses = models.ManyToManyField(ScreeningRoom)
    screening_start_date = models.DateField()
    screening_end_date = models.DateField()
    type = "Send DCP"


class EncodeDVDJob(Job):
    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Requested'),
        (50, 'In Progress'),
        (100, 'Finished'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    VIDEO_FORMAT_CHOICES = (
        ('NTSC', 'NTSC'),
        ('PAL', 'PAL'),
    )
    video_format = models.CharField(choices=VIDEO_FORMAT_CHOICES, default='NTSC', max_length=10)

    type = "Encode DVD"

    def get_price(self):
        if self.asset.content_type == "FTR":
            return 200
        if self.asset.content_type == "SHR30":
            return 115
        if self.asset.content_type == "SHR15":
            return 50


class EncodeBlurayJob(Job):
    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Requested'),
        (50, 'In Progress'),
        (100, 'Finished'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    type = "Encode Bluray"

    def get_price(self):
        if self.asset.content_type == "FTR":
            return 325
        if self.asset.content_type == "SHR30":
            return 160
        if self.asset.content_type == "SHR15":
            return 75


