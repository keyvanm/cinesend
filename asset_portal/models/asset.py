import string

from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.fields import AutoSlugField
from model_utils.fields import MonitorField
from django.contrib.auth.models import User
from durationfield.db.models.fields.duration import DurationField
from model_utils.models import TimeStampedModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.crypto import get_random_string

from utils import posters_unique_filename


def generate_tracking_code():
    code = get_random_string(10, allowed_chars=string.digits).upper()
    if Asset.objects.filter(tracking_number=code):
        return generate_tracking_code()
    return code


class TrackingNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        kwargs['unique'] = True
        kwargs['editable'] = False
        super(TrackingNumberField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add:
            value = generate_tracking_code()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(TrackingNumberField, self).pre_save(model_instance, add)


class Asset(TimeStampedModel):
    made_by = models.ForeignKey(User, related_name='assets_created')
    owners = models.ManyToManyField(User, related_name='assets_owned', null=True, blank=True)

    @property
    def title(self):
        return self.film_title

    slug = AutoSlugField(populate_from=('title', 'version_name', 'release_year'), unique=True)

    STATUS_CHOICES = (
        (0, 'Error'),
        (1, 'Awaiting Content'),
        (33, 'Received'),
        (66, 'Pending'),
        (100, 'Online'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    status_changed = MonitorField(monitor='status', editable=False)
    deleted = models.BooleanField(default=False)

    @property
    def type(self):
        return self.content_type

    # -----------------------------------------------------------------------------------------------------

    # created_by_job = models.ForeignKey(Job, null=True, blank=True)
    tracking_number = TrackingNumberField()

    @property
    def tracking_number_display(self):
        return "{0} - {1} - {2}".format(self.tracking_number[:4], self.tracking_number[4:6], self.tracking_number[6:])

    film_title = models.CharField(max_length=200)
    version_name = models.CharField(max_length=200, default="Original")
    CONTENT_TYPE_CHOICES = (
        ('FTR', 'Feature'),
        # ('TLR', 'Trailer'),
        # ('TSR', 'Teaser'),
        # ('PRO', 'Promo'),
        # ('TST', 'Test Content'),
        # ('RTG', 'Rating Tag'),
        ('SHR15', 'Short (Under 15 mins)'),
        ('SHR30', 'Short (16-30 mins)'),
        # ('ADV', 'Advertisement'),
        # ('XSN', 'Transitional'),
        # ('PSA', 'Public Service Announcement'),
        # ('POL', 'Policy Trailer'),
    )
    content_type = models.CharField(choices=CONTENT_TYPE_CHOICES, max_length=50)
    release_year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2050)])
    running_time = DurationField(blank=True, null=True)

    poster = models.ImageField(upload_to=posters_unique_filename, blank=True)
    LANG_CODES = (
        ('SQ', 'SQ - ALBANIAN'),
        ('AR', 'AR - ARABIC'),
        ('BS', 'BS - BOSNIAN'),
        ('BG', 'BG - BULGARIAN'),
        ('CA', 'CA - CATALAN'),
        ('YUE', 'YUE - CHINESE - CANTONESE'),
        ('HR', 'HR - CROATIAN'),
        ('CS', 'CS - CZECH'),
        ('DA', 'DA - DANISH'),
        ('NL', 'NL - DUTCH'),
        ('EN', 'EN - ENGLISH'),
        ('ET', 'ET - ESTONIAN'),
        ('EU', 'EU - EUSKARA'),
        ('FI', 'FI - FINNISH'),
        ('VLS', 'VLS - FLEMISH'),
        ('FR', 'FR - FRENCH'),
        ('QFC', 'QFC - FRENCH - CANADIAN'),
        ('DE', 'DE - GERMAN'),
        ('GSW', 'GSW - GERMAN - SWISS'),
        ('EL', 'EL - GREEK'),
        ('HE', 'HE - HEBREW'),
        ('HI', 'HI - HINDI'),
        ('HU', 'HU - HUNGARIAN'),
        ('IS', 'IS - ICELANDIC'),
        ('IND', 'IND - INDONESIAN BAHASA'),
        ('IT', 'IT - ITALIAN'),
        ('JA', 'JA - JAPANESE'),
        ('KK', 'KK - KAZAKH'),
        ('KO', 'KO - KOREAN'),
        ('LV', 'LV - LATVIAN'),
        ('LT', 'LT - LITHUANIAN'),
        ('MSA', 'MSA - MALAY BAHASA'),
        ('MN', 'MN - MONGOLIAN'),
        ('NO', 'NO - NORWEGIAN'),
        ('PL', 'PL - POLISH'),
        ('QBP', 'QBP - PORTUGUESE - BRAZILIAN'),
        ('PT', 'PT - PORTUGUESE - EUROPEAN'),
        ('RO', 'RO - ROMANIAN'),
        ('RU', 'RU - RUSSIAN'),
        ('SR', 'SR - SERBIAN'),
        ('SK', 'SK - SLOVAK'),
        ('SL', 'SL - SLOVENIAN'),
        ('QSA', 'QSA - SPANISH - ARGENTINIAN'),
        ('ES', 'ES - SPANISH - CASTILIAN'),
        ('LAS', 'LAS - SPANISH - LATIN AMERICAN'),
        ('QSM', 'QSM - SPANISH - MEXICAN'),
        ('SV', 'SV - SWEDISH'),
        ('TA', 'TA - TAMIL'),
        ('TE', 'TE - TELUGU'),
        ('TH', 'TH - THAI'),
        ('TR', 'TR - TURKISH'),
        ('UK', 'UK - UKRAINIAN'),
        ('VI', 'VI - VIETNAMESE'),
        ('WEL', 'WEL - WELSH (CYMRU)'),
    )
    AUDIO_LANG_CHOICES = LANG_CODES + (
        ('NAN', 'NAN - CHINESE - TAIWANESE (Audio Only)'),
        ('QTM', 'QTM - CHINESE - TAIWANESE MANDARIN (Audio Only)'),
        ('CMN', 'CMN - CHINESE - MANDARIN PRC (Audio Only)'),
        ('XX', 'XX - NO SPOKEN LANGUAGE'),
    )
    audio_language = models.CharField(choices=AUDIO_LANG_CHOICES, max_length=50)

    SUBTITLE_LANG_CHOICES = LANG_CODES + (
        ('QMS', 'QMS - CHINESE - MANDARIN SIMPLIFIED (Subtitles Only)'),
        ('QMT', 'QMT - CHINESE - MANDARIN TRADITIONAL (Subtitles Only)'),
        ('XX', 'XX - NO SUBTITLE'),
    )
    subtitle_language = models.CharField(choices=SUBTITLE_LANG_CHOICES, max_length=50)

    TERRITORY_CHOICES = (
        ('AL', 'AL - ALBANIA'),
        ('AR', 'AR - ARGENTINA'),
        ('AW', 'AW - ARUBA'),
        ('AU', 'AU - AUSTRALIA'),
        ('AT', 'AT - AUSTRIA'),
        ('BH', 'BH - BAHRAIN'),
        ('BY', 'BY - BELARUS'),
        ('BE', 'BE - BELGIUM'),
        ('BZ', 'BZ - BELIZE'),
        ('BO', 'BO - BOLIVIA'),
        ('BA', 'BA - BOSNIA/HERZ'),
        ('BR', 'BR - BRAZIL'),
        ('BG', 'BG - BULGARIA'),
        ('KH', 'KH - CAMBODIA'),
        ('CA', 'CA - CANADA'),
        ('CL', 'CL - CHILE'),
        ('CN', 'CN - CHINA'),
        ('CO', 'CO - COLOMBIA'),
        ('CR', 'CR - COSTA RICA'),
        ('HR', 'HR - CROATIA'),
        ('AN', 'AN - CURACAO'),
        ('CY', 'CY - CYPRUS'),
        ('CZ', 'CZ - CZECH REPUBLIC'),
        ('DK', 'DK - DENMARK'),
        ('DO', 'DO - DOMINICAN REPUBLIC'),
        ('DU', 'DU - DUBAI'),
        ('EC', 'EC - ECUADOR'),
        ('EG', 'EG - EGYPT'),
        ('SV', 'SV - EL SALVADOR'),
        ('EE', 'EE - ESTONIA'),
        ('ET', 'ET - ETHIOPIA'),
        ('FI', 'FI - FINLAND'),
        ('FR', 'FR - FRANCE'),
        ('PF', 'PF - FRENCH POLYNESIA'),
        ('DE', 'DE - GERMANY'),
        ('GH', 'GH - GHANA'),
        ('GR', 'GR - GREECE'),
        ('GP', 'GP - GUADELOUPE'),
        ('GT', 'GT - GUATEMALA'),
        ('HN', 'HN - HONDURAS'),
        ('HK', 'HK - HONG KONG'),
        ('HU', 'HU - HUNGARY'),
        ('IS', 'IS - ICELAND'),
        ('IN', 'IN - INDIA'),
        ('ID', 'ID - INDONESIA'),
        ('IQ', 'IQ - IRAQ'),
        ('IE', 'IE - IRELAND'),
        ('IL', 'IL - ISRAEL'),
        ('IT', 'IT - ITALY'),
        ('JM', 'JM - JAMAICA'),
        ('JP', 'JP - JAPAN'),
        ('JO', 'JO - JORDAN'),
        ('KZ', 'KZ - KAZAKHSTAN'),
        ('KE', 'KE - KENYA'),
        ('KW', 'KW - KUWAIT'),
        ('LV', 'LV - LATVIA'),
        ('LB', 'LB - LEBANON'),
        ('LT', 'LT - LITHUANIA'),
        ('LU', 'LU - LUXEMBOURG'),
        ('MK', 'MK - MACEDONIA'),
        ('MY', 'MY - MALAYSIA'),
        ('MT', 'MT - MALTA'),
        ('MQ', 'MQ - MARTINIQUE'),
        ('MU', 'MU - MAURITIUS'),
        ('MX', 'MX - MEXICO'),
        ('MD', 'MD - MOLDOVA'),
        ('MN', 'MN - MONGOLIA'),
        ('ME', 'ME - MONTENEGRO'),
        ('MA', 'MA - MOROCCO'),
        ('MM', 'MM - MYANMAR'),
        ('NP', 'NP - NEPAL'),
        ('NL', 'NL - NETHERLANDS'),
        ('NC', 'NC - NEW CALEDONIA'),
        ('NZ', 'NZ - NEW ZEALAND'),
        ('NI', 'NI - NICARAGUA'),
        ('NG', 'NG - NIGERIA'),
        ('NO', 'NO - NORWAY'),
        ('OM', 'OM - OMAN'),
        ('PK', 'PK - PAKISTAN'),
        ('PA', 'PA - PANAMA'),
        ('PY', 'PY - PARAGUAY'),
        ('PE', 'PE - PERU'),
        ('PH', 'PH - PHILIPPINES'),
        ('PL', 'PL - POLAND'),
        ('PT', 'PT - PORTUGAL'),
        ('QA', 'QA - QATAR'),
        ('RE', 'RE - REUNION'),
        ('RO', 'RO - ROMANIA'),
        ('RU', 'RU - RUSSIA'),
        ('SA', 'SA - SAUDI ARABIA'),
        ('SN', 'SN - SENEGAL'),
        ('CS', 'CS - SERBIA'),
        ('SG', 'SG - SINGAPORE'),
        ('SK', 'SK - SLOVAKIA'),
        ('SI', 'SI - SLOVENIA'),
        ('ZA', 'ZA - SOUTH AFRICA'),
        ('KR', 'KR - SOUTH KOREA'),
        ('ES', 'ES - SPAIN'),
        ('LK', 'LK - SRI LANKA'),
        ('SE', 'SE - SWEDEN'),
        ('CH', 'CH - SWITZERLAND'),
        ('SY', 'SY - SYRIAN ARAB REPUBLIC'),
        ('TW', 'TW - TAIWAN'),
        ('TZ', 'TZ - TANZANIA'),
        ('TH', 'TH - THAILAND'),
        ('TT', 'TT - TRINIDAD'),
        ('TN', 'TN - TUNISIA'),
        ('TR', 'TR - TURKEY'),
        ('UA', 'UA - UKRAINE'),
        ('AE', 'AE - UNITED ARAB EMIRATES'),
        ('UK', 'UK - UNITED KINGDOM'),
        ('US', 'US - UNITED STATES'),
        ('UY', 'UY - URUGUAY'),
        ('VE', 'VE - VENEZUELA'),
        ('VN', 'VN - VIETNAM'),
    )
    territory = models.CharField(choices=TERRITORY_CHOICES, max_length=50)

    RATING_CHOICES = (
        ("NR", "NR - Not Rated"),
        ("G", "G"),
        ("NC", "NC-17"),
        ("PG", "PG"),
        ("13", "PG-13"),
        ("R", "R"),
        # ("GB", "GB - Green Band"),
        # ("RB", "RB - Red Band"),
    )
    rating = models.CharField(choices=RATING_CHOICES, max_length=50)

    studio = models.CharField(max_length=200)

    temp_version = models.BooleanField(default=False)
    pre_release_version = models.BooleanField(default=False)
    red_band_content = models.BooleanField(default=False)

    DIMENSION_CHOICES = (
        ('2D', '2D Content'),
        ('3D', '3D Content'),
        ('2D3D', '2D Version of 3D Content'),
    )
    dimension_properties = models.CharField(choices=DIMENSION_CHOICES, max_length=50, verbose_name="2D/3D")

    RES_CHOICES = (
        ("FULL_HD", "Full HD - 1920x1080 (1.77:1)"),
        ("TWO_K_SCOPE", "2K Scope - 2048x858 (2.39:1)"),
        ("TWO_K_FLAT", "2K Flat - 1998x1080 (1.85:1)"),
        ("TWO_K_FULL", "2K Full - 2048x1080 (1.90:1)"),
        ("FOUR_K_SCOPE", "4K Scope - 4096x1716 (2.39:1)"),
        ("FOUR_K_FLAT", "4K Flat - 3996x2160 (1.85:1)"),
        ("FOUR_K_FULL", "4K Full - 4906x2160 (1.90:1)"),
    )
    source_resolution = models.CharField(choices=RES_CHOICES, max_length=50)

    FRAME_RATE_CHOICES = (
        ("24", "24 fps"),
        ("25", "25 fps"),
        ("2398", "23.98 fps"),
        ("2997", "29.97 fps"),
        ("48", "48 fps"),
        ("4795", "47.95 fps"),
        ("60i", "60i"),
    )
    frame_rate = models.CharField(choices=FRAME_RATE_CHOICES, max_length=50, verbose_name="Source frame rate")

    COLORSPACE_CHOICES = (
        ("UNKNOWN", "I'm not sure"),
        ("REC_709", "Rec.709"),
        ("DCI", "DCI P3"),
    )
    source_colorspace = models.CharField(choices=COLORSPACE_CHOICES, max_length=50)

    AUDIO_FORMAT_CHOICES = (
        ("MONO", "Mono (1 channel)"),
        ("STEREO", "Stereo (L, R)"),
        ("THREE_CHANNEL", "Three-channel (L, C, R)"),
        ("FIVE_ONE", "5.1 (C, L, R, Lfe, Ls, Rs)"),
        ("SEVEN_ONE", "7.1 (C,L,R,Lfe, Ls, Rs, Lb, Rb)"),
        ("DOLBY_ATMOS", "Dolby Atmos"),
    )
    source_audio_format = models.CharField(choices=AUDIO_FORMAT_CHOICES, max_length=50)

    imax_content = models.BooleanField(default=False, verbose_name="IMAX Content")
    dbox_content = models.BooleanField(default=False, verbose_name="D-BOX Content")
    closed_captioned = models.BooleanField(default=False, verbose_name="Closed Captioned")
    ACCESSIBLE_AUDIO_CHOICES = (
        ("NONE", "None"),
        ("HI", "HI: Hearing Impaired"),
        ("VI-N", "VI-N: Visually Impaired Narrative"),
        ("HI+VI-N", "HI + VI-N"),
    )
    accessible_audio = models.CharField(choices=ACCESSIBLE_AUDIO_CHOICES, default="NONE", max_length=50)

    FILE_TYPE_CHOICES = (
        ('ProRes 4444', 'ProRes 4444'),
        ('ProRes 422HQ', 'ProRes 422HQ'),
        ('DNxHD', 'DNxHD'),
        ('TIFF Sequence', 'TIFF Sequence'),
        ('DPX Sequence', 'DPX Sequence'),
    )
    file_type = models.CharField(choices=FILE_TYPE_CHOICES, max_length=50, blank=True)
    notes = models.TextField(blank=True)
    is_title_safe = models.NullBooleanField()

    def __unicode__(self):
        return u'Asset %s - %s (%s)' % (self.film_title, self.version_name, self.release_year)

    @property
    def full_name(self):
        return u'%s - %s (%s)' % (self.film_title, self.version_name, self.release_year)

    def get_absolute_url(self):
        return reverse('asset-detail', kwargs={'slug': self.slug})

    class Meta:
        app_label = "asset_portal"
