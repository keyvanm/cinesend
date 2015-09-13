from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from durationfield.db.models.fields.duration import DurationField
from model_utils.choices import Choices
from asset_portal.models.asset import Asset
from asset_portal.models.job import EncodeDVDJob, EncodeBlurayJob


class AbstractOpticalDisc(TimeStampedModel):
    asset = models.ForeignKey(Asset, related_name='+')

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=('asset', 'title'), unique=True)

    running_time = DurationField()
    FRAME_RATE_CHOICES = Choices(
        ("24", "24 fps"),
        ("25", "25 fps"),
        ("30", "30 fps"),
        ("48", "48 fps"),
        ("50", "50 fps"),
        ("60", "60 fps"),
    )
    frame_rate = models.CharField(choices=FRAME_RATE_CHOICES, max_length=50)

    ASPECT_RATIO_CHOICES = Choices(
        ("43", "4:3"),
        ("169", "16:9")
    )
    aspect_ratio = models.CharField(choices=ASPECT_RATIO_CHOICES, max_length=50)

    AUDIO_TRACK_CHOICES = Choices(
        ("2Discreet", "2.0 Discreet"),
        ("51Discreet", "5.1 Discreet"),
        ("51Dolby", "5.1 Dolby Prologic II"),
        ("51DTS", "5.1 DTS")
    )
    audio_track_1 = models.CharField(choices=AUDIO_TRACK_CHOICES, max_length=50)
    audio_track_2 = models.CharField(choices=AUDIO_TRACK_CHOICES, max_length=50, blank=True)

    audio_language = models.CharField(choices=Asset.AUDIO_LANG_CHOICES, max_length=50)
    subtitle_language = models.CharField(choices=Asset.SUBTITLE_LANG_CHOICES, max_length=50)

    SUBTITLE_TYPE_CHOICES = Choices(
        ('burnin', 'Burn-in'),
        ('external', 'External'),
    )
    subtitle_type = models.CharField(choices=SUBTITLE_TYPE_CHOICES, max_length=50)

    letterboxed = models.BooleanField(default=False)
    pillarboxed = models.BooleanField(default=False)

    class Meta:
        abstract = True



class DVD(AbstractOpticalDisc):
    job = models.OneToOneField(EncodeDVDJob)
    REGION_CHOICES = Choices(
        ('ntsc', 'NTSC'),
        ('pal', 'PAL'),
    )
    region = models.CharField(choices=REGION_CHOICES, max_length=50)

class Bluray(AbstractOpticalDisc):
    job = models.OneToOneField(EncodeBlurayJob)
    ENCODING_CHOICES = Choices(
        ('mpeg2', 'MPEG 2'),
        ('h264', 'H.264'),
    )
    encoding = models.CharField(choices=ENCODING_CHOICES, max_length=50)

    RESOLUTION_CHOICES = Choices(
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    resolution = models.CharField(choices=RESOLUTION_CHOICES, max_length=50)
