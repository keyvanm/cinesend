from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from durationfield.db.models.fields.duration import DurationField
from model_utils.choices import Choices
from sizefield.models import FileSizeField
from asset_portal.models.asset import Asset
from asset_portal.models.job import MakeDCPJob
from livefield.fields import LiveField
from livefield.managers import LiveManager


class DCP(TimeStampedModel):
    job = models.OneToOneField(MakeDCPJob)
    asset = models.ForeignKey(Asset)

    slug = AutoSlugField(populate_from=('asset', 'version_name'), unique=True)
    live = LiveField()

    objects = LiveManager()
    all_objects = LiveManager(include_soft_deleted=True)

    def delete(self, using=None):
        self.soft_delete()

    def hard_delete(self, using=None):  # pylint: disable=super-on-old-class
        super(DCP, self).delete(using)

    def soft_delete(self):
        self.live = False
        self.save()

    version_name = models.CharField(max_length=200, default="Original")


    DIMENSION_CHOICES = (
        ('2D', '2D Content'),
        ('3D', '3D Content'),
    )
    dimension_properties = models.CharField(choices=DIMENSION_CHOICES, max_length=50, verbose_name="2D/3D")

    # file_path_on_nas = models.FilePathField() # TODO:
    file_size = FileSizeField()

    STANDARD_CHOICES = Choices(
        ('smpte', 'SMPTE'),
        ('interop', 'Interop'),
    )
    dcp_standard = models.CharField(choices=STANDARD_CHOICES, max_length=20)
    FRAME_RATE_CHOICES = Choices(
        ("24", "24 fps"),
        ("25", "25 fps"),
        ("30", "30 fps"),
        ("48", "48 fps"),
        ("50", "50 fps"),
        ("60", "60 fps"),
    )
    frame_rate = models.CharField(choices=FRAME_RATE_CHOICES, max_length=50)

    CONTAINER_CHOICES = Choices(
        ('2kflat', '2K Flat'),
        ('2kscope', '2K Scope'),
        ('4kflat', '4K Flat'),
        ('4kscope', '4K Scope'),
    )
    container = models.CharField(choices=CONTAINER_CHOICES, max_length=50)

    running_time = DurationField()
    credit_offset = DurationField(blank=True, null=True)

    pkl_name = models.CharField(max_length=255, verbose_name='PKL Name')
    composition_name = models.CharField(max_length=255)
    number_of_reels = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    ISSUER_CHOICES = Choices(
        ('bitcine', 'BitCine Technologies'),
    )
    issuer = models.CharField(choices=ISSUER_CHOICES, max_length=255, default='bitcine')

    SUBTITLE_TYPE_CHOICES = Choices(
        ('burnin', 'Burn-in'),
        ('smpte', 'SMPTE'),
        ('interop', 'Interop'),
    )
    subtitle_type = models.CharField(choices=SUBTITLE_TYPE_CHOICES, max_length=50, blank=True)

    def __unicode__(self):
        return u'DCP file for {0} - version {1}'.format(self.asset, self.version_name)

    class Meta:
        app_label = 'vault'
        verbose_name = 'DCP'