# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration
import model_utils.fields
import django_extensions.db.fields
import asset_portal.models.utils
import asset_portal.models.asset
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'title', b'version_name', b'release_year'), blank=True, unique=True)),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Awaiting Content'), (33, b'Received'), (66, b'Pending'), (100, b'Online')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor=b'status')),
                ('deleted', models.BooleanField(default=False)),
                ('tracking_number', asset_portal.models.asset.TrackingNumberField(unique=True, max_length=10, editable=False)),
                ('film_title', models.CharField(max_length=200)),
                ('version_name', models.CharField(default=b'Original', max_length=200)),
                ('content_type', models.CharField(max_length=50, choices=[(b'FTR', b'Feature'), (b'SHR15', b'Short (Under 15 mins)'), (b'SHR30', b'Short (16-30 mins)')])),
                ('release_year', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)])),
                ('running_time', durationfield.db.models.fields.duration.DurationField(null=True, blank=True)),
                ('poster', models.ImageField(upload_to=asset_portal.models.utils.UniqueFilename(b'posters'), blank=True)),
                ('audio_language', models.CharField(max_length=50, choices=[(b'SQ', b'SQ - ALBANIAN'), (b'AR', b'AR - ARABIC'), (b'BS', b'BS - BOSNIAN'), (b'BG', b'BG - BULGARIAN'), (b'CA', b'CA - CATALAN'), (b'YUE', b'YUE - CHINESE - CANTONESE'), (b'HR', b'HR - CROATIAN'), (b'CS', b'CS - CZECH'), (b'DA', b'DA - DANISH'), (b'NL', b'NL - DUTCH'), (b'EN', b'EN - ENGLISH'), (b'ET', b'ET - ESTONIAN'), (b'EU', b'EU - EUSKARA'), (b'FI', b'FI - FINNISH'), (b'VLS', b'VLS - FLEMISH'), (b'FR', b'FR - FRENCH'), (b'QFC', b'QFC - FRENCH - CANADIAN'), (b'DE', b'DE - GERMAN'), (b'GSW', b'GSW - GERMAN - SWISS'), (b'EL', b'EL - GREEK'), (b'HE', b'HE - HEBREW'), (b'HI', b'HI - HINDI'), (b'HU', b'HU - HUNGARIAN'), (b'IS', b'IS - ICELANDIC'), (b'IND', b'IND - INDONESIAN BAHASA'), (b'IT', b'IT - ITALIAN'), (b'JA', b'JA - JAPANESE'), (b'KK', b'KK - KAZAKH'), (b'KO', b'KO - KOREAN'), (b'LV', b'LV - LATVIAN'), (b'LT', b'LT - LITHUANIAN'), (b'MSA', b'MSA - MALAY BAHASA'), (b'MN', b'MN - MONGOLIAN'), (b'NO', b'NO - NORWEGIAN'), (b'PL', b'PL - POLISH'), (b'QBP', b'QBP - PORTUGUESE - BRAZILIAN'), (b'PT', b'PT - PORTUGUESE - EUROPEAN'), (b'RO', b'RO - ROMANIAN'), (b'RU', b'RU - RUSSIAN'), (b'SR', b'SR - SERBIAN'), (b'SK', b'SK - SLOVAK'), (b'SL', b'SL - SLOVENIAN'), (b'QSA', b'QSA - SPANISH - ARGENTINIAN'), (b'ES', b'ES - SPANISH - CASTILIAN'), (b'LAS', b'LAS - SPANISH - LATIN AMERICAN'), (b'QSM', b'QSM - SPANISH - MEXICAN'), (b'SV', b'SV - SWEDISH'), (b'TA', b'TA - TAMIL'), (b'TE', b'TE - TELUGU'), (b'TH', b'TH - THAI'), (b'TR', b'TR - TURKISH'), (b'UK', b'UK - UKRAINIAN'), (b'VI', b'VI - VIETNAMESE'), (b'WEL', b'WEL - WELSH (CYMRU)'), (b'NAN', b'NAN - CHINESE - TAIWANESE (Audio Only)'), (b'QTM', b'QTM - CHINESE - TAIWANESE MANDARIN (Audio Only)'), (b'CMN', b'CMN - CHINESE - MANDARIN PRC (Audio Only)'), (b'XX', b'XX - NO SPOKEN LANGUAGE')])),
                ('subtitle_language', models.CharField(max_length=50, choices=[(b'SQ', b'SQ - ALBANIAN'), (b'AR', b'AR - ARABIC'), (b'BS', b'BS - BOSNIAN'), (b'BG', b'BG - BULGARIAN'), (b'CA', b'CA - CATALAN'), (b'YUE', b'YUE - CHINESE - CANTONESE'), (b'HR', b'HR - CROATIAN'), (b'CS', b'CS - CZECH'), (b'DA', b'DA - DANISH'), (b'NL', b'NL - DUTCH'), (b'EN', b'EN - ENGLISH'), (b'ET', b'ET - ESTONIAN'), (b'EU', b'EU - EUSKARA'), (b'FI', b'FI - FINNISH'), (b'VLS', b'VLS - FLEMISH'), (b'FR', b'FR - FRENCH'), (b'QFC', b'QFC - FRENCH - CANADIAN'), (b'DE', b'DE - GERMAN'), (b'GSW', b'GSW - GERMAN - SWISS'), (b'EL', b'EL - GREEK'), (b'HE', b'HE - HEBREW'), (b'HI', b'HI - HINDI'), (b'HU', b'HU - HUNGARIAN'), (b'IS', b'IS - ICELANDIC'), (b'IND', b'IND - INDONESIAN BAHASA'), (b'IT', b'IT - ITALIAN'), (b'JA', b'JA - JAPANESE'), (b'KK', b'KK - KAZAKH'), (b'KO', b'KO - KOREAN'), (b'LV', b'LV - LATVIAN'), (b'LT', b'LT - LITHUANIAN'), (b'MSA', b'MSA - MALAY BAHASA'), (b'MN', b'MN - MONGOLIAN'), (b'NO', b'NO - NORWEGIAN'), (b'PL', b'PL - POLISH'), (b'QBP', b'QBP - PORTUGUESE - BRAZILIAN'), (b'PT', b'PT - PORTUGUESE - EUROPEAN'), (b'RO', b'RO - ROMANIAN'), (b'RU', b'RU - RUSSIAN'), (b'SR', b'SR - SERBIAN'), (b'SK', b'SK - SLOVAK'), (b'SL', b'SL - SLOVENIAN'), (b'QSA', b'QSA - SPANISH - ARGENTINIAN'), (b'ES', b'ES - SPANISH - CASTILIAN'), (b'LAS', b'LAS - SPANISH - LATIN AMERICAN'), (b'QSM', b'QSM - SPANISH - MEXICAN'), (b'SV', b'SV - SWEDISH'), (b'TA', b'TA - TAMIL'), (b'TE', b'TE - TELUGU'), (b'TH', b'TH - THAI'), (b'TR', b'TR - TURKISH'), (b'UK', b'UK - UKRAINIAN'), (b'VI', b'VI - VIETNAMESE'), (b'WEL', b'WEL - WELSH (CYMRU)'), (b'QMS', b'QMS - CHINESE - MANDARIN SIMPLIFIED (Subtitles Only)'), (b'QMT', b'QMT - CHINESE - MANDARIN TRADITIONAL (Subtitles Only)'), (b'XX', b'XX - NO SUBTITLE')])),
                ('territory', models.CharField(max_length=50, choices=[(b'AL', b'AL - ALBANIA'), (b'AR', b'AR - ARGENTINA'), (b'AW', b'AW - ARUBA'), (b'AU', b'AU - AUSTRALIA'), (b'AT', b'AT - AUSTRIA'), (b'BH', b'BH - BAHRAIN'), (b'BY', b'BY - BELARUS'), (b'BE', b'BE - BELGIUM'), (b'BZ', b'BZ - BELIZE'), (b'BO', b'BO - BOLIVIA'), (b'BA', b'BA - BOSNIA/HERZ'), (b'BR', b'BR - BRAZIL'), (b'BG', b'BG - BULGARIA'), (b'KH', b'KH - CAMBODIA'), (b'CA', b'CA - CANADA'), (b'CL', b'CL - CHILE'), (b'CN', b'CN - CHINA'), (b'CO', b'CO - COLOMBIA'), (b'CR', b'CR - COSTA RICA'), (b'HR', b'HR - CROATIA'), (b'AN', b'AN - CURACAO'), (b'CY', b'CY - CYPRUS'), (b'CZ', b'CZ - CZECH REPUBLIC'), (b'DK', b'DK - DENMARK'), (b'DO', b'DO - DOMINICAN REPUBLIC'), (b'DU', b'DU - DUBAI'), (b'EC', b'EC - ECUADOR'), (b'EG', b'EG - EGYPT'), (b'SV', b'SV - EL SALVADOR'), (b'EE', b'EE - ESTONIA'), (b'ET', b'ET - ETHIOPIA'), (b'FI', b'FI - FINLAND'), (b'FR', b'FR - FRANCE'), (b'PF', b'PF - FRENCH POLYNESIA'), (b'DE', b'DE - GERMANY'), (b'GH', b'GH - GHANA'), (b'GR', b'GR - GREECE'), (b'GP', b'GP - GUADELOUPE'), (b'GT', b'GT - GUATEMALA'), (b'HN', b'HN - HONDURAS'), (b'HK', b'HK - HONG KONG'), (b'HU', b'HU - HUNGARY'), (b'IS', b'IS - ICELAND'), (b'IN', b'IN - INDIA'), (b'ID', b'ID - INDONESIA'), (b'IQ', b'IQ - IRAQ'), (b'IE', b'IE - IRELAND'), (b'IL', b'IL - ISRAEL'), (b'IT', b'IT - ITALY'), (b'JM', b'JM - JAMAICA'), (b'JP', b'JP - JAPAN'), (b'JO', b'JO - JORDAN'), (b'KZ', b'KZ - KAZAKHSTAN'), (b'KE', b'KE - KENYA'), (b'KW', b'KW - KUWAIT'), (b'LV', b'LV - LATVIA'), (b'LB', b'LB - LEBANON'), (b'LT', b'LT - LITHUANIA'), (b'LU', b'LU - LUXEMBOURG'), (b'MK', b'MK - MACEDONIA'), (b'MY', b'MY - MALAYSIA'), (b'MT', b'MT - MALTA'), (b'MQ', b'MQ - MARTINIQUE'), (b'MU', b'MU - MAURITIUS'), (b'MX', b'MX - MEXICO'), (b'MD', b'MD - MOLDOVA'), (b'MN', b'MN - MONGOLIA'), (b'ME', b'ME - MONTENEGRO'), (b'MA', b'MA - MOROCCO'), (b'MM', b'MM - MYANMAR'), (b'NP', b'NP - NEPAL'), (b'NL', b'NL - NETHERLANDS'), (b'NC', b'NC - NEW CALEDONIA'), (b'NZ', b'NZ - NEW ZEALAND'), (b'NI', b'NI - NICARAGUA'), (b'NG', b'NG - NIGERIA'), (b'NO', b'NO - NORWAY'), (b'OM', b'OM - OMAN'), (b'PK', b'PK - PAKISTAN'), (b'PA', b'PA - PANAMA'), (b'PY', b'PY - PARAGUAY'), (b'PE', b'PE - PERU'), (b'PH', b'PH - PHILIPPINES'), (b'PL', b'PL - POLAND'), (b'PT', b'PT - PORTUGAL'), (b'QA', b'QA - QATAR'), (b'RE', b'RE - REUNION'), (b'RO', b'RO - ROMANIA'), (b'RU', b'RU - RUSSIA'), (b'SA', b'SA - SAUDI ARABIA'), (b'SN', b'SN - SENEGAL'), (b'CS', b'CS - SERBIA'), (b'SG', b'SG - SINGAPORE'), (b'SK', b'SK - SLOVAKIA'), (b'SI', b'SI - SLOVENIA'), (b'ZA', b'ZA - SOUTH AFRICA'), (b'KR', b'KR - SOUTH KOREA'), (b'ES', b'ES - SPAIN'), (b'LK', b'LK - SRI LANKA'), (b'SE', b'SE - SWEDEN'), (b'CH', b'CH - SWITZERLAND'), (b'SY', b'SY - SYRIAN ARAB REPUBLIC'), (b'TW', b'TW - TAIWAN'), (b'TZ', b'TZ - TANZANIA'), (b'TH', b'TH - THAILAND'), (b'TT', b'TT - TRINIDAD'), (b'TN', b'TN - TUNISIA'), (b'TR', b'TR - TURKEY'), (b'UA', b'UA - UKRAINE'), (b'AE', b'AE - UNITED ARAB EMIRATES'), (b'UK', b'UK - UNITED KINGDOM'), (b'US', b'US - UNITED STATES'), (b'UY', b'UY - URUGUAY'), (b'VE', b'VE - VENEZUELA'), (b'VN', b'VN - VIETNAM')])),
                ('rating', models.CharField(max_length=50, choices=[(b'NR', b'NR - Not Rated'), (b'G', b'G'), (b'NC', b'NC-17'), (b'PG', b'PG'), (b'13', b'PG-13'), (b'R', b'R')])),
                ('studio', models.CharField(max_length=200)),
                ('temp_version', models.BooleanField(default=False)),
                ('pre_release_version', models.BooleanField(default=False)),
                ('red_band_content', models.BooleanField(default=False)),
                ('dimension_properties', models.CharField(max_length=50, verbose_name=b'2D/3D', choices=[(b'2D', b'2D Content'), (b'3D', b'3D Content'), (b'2D3D', b'2D Version of 3D Content')])),
                ('source_resolution', models.CharField(max_length=50, choices=[(b'FULL_HD', b'Full HD - 1920x1080 (1.77:1)'), (b'TWO_K_SCOPE', b'2K Scope - 2048x858 (2.39:1)'), (b'TWO_K_FLAT', b'2K Flat - 1998x1080 (1.85:1)'), (b'TWO_K_FULL', b'2K Full - 2048x1080 (1.90:1)'), (b'FOUR_K_SCOPE', b'4K Scope - 4096x1716 (2.39:1)'), (b'FOUR_K_FLAT', b'4K Flat - 3996x2160 (1.85:1)'), (b'FOUR_K_FULL', b'4K Full - 4906x2160 (1.90:1)')])),
                ('frame_rate', models.CharField(max_length=50, verbose_name=b'Source frame rate', choices=[(b'24', b'24 fps'), (b'25', b'25 fps'), (b'2398', b'23.98 fps'), (b'2997', b'29.97 fps'), (b'48', b'48 fps'), (b'4795', b'47.95 fps'), (b'60i', b'60i')])),
                ('source_colorspace', models.CharField(max_length=50, choices=[(b'UNKNOWN', b"I'm not sure"), (b'REC_709', b'Rec.709'), (b'DCI', b'DCI')])),
                ('source_audio_format', models.CharField(max_length=50, choices=[(b'MONO', b'Mono (1 channel)'), (b'STEREO', b'Stereo (L, R)'), (b'THREE_CHANNEL', b'Three-channel (L, C, R)'), (b'FIVE_ONE', b'5.1 (C, L, R, Lfe, Ls, Rs)'), (b'SEVEN_ONE', b'7.1 (C,L,R,Lfe, Ls, Rs, Lb, Rb)'), (b'DOLBY_ATMOS', b'Dolby Atmos')])),
                ('imax_content', models.BooleanField(default=False, verbose_name=b'IMAX Content')),
                ('dbox_content', models.BooleanField(default=False, verbose_name=b'D-BOX Content')),
                ('closed_captioned', models.BooleanField(default=False, verbose_name=b'Closed Captioned')),
                ('accessible_audio', models.CharField(default=b'NONE', max_length=50, choices=[(b'NONE', b'None'), (b'HI', b'HI: Hearing Impaired'), (b'VI-N', b'VI-N: Visually Impaired Narrative'), (b'HI+VI-N', b'HI + VI-N')])),
                ('file_type', models.CharField(max_length=50, choices=[(b'ProRes 4444', b'ProRes 4444'), (b'ProRes 422HQ', b'ProRes 422HQ'), (b'DNxHD', b'DNxHD'), (b'TIFF Sequence', b'TIFF Sequence'), (b'DPX Sequence', b'DPX Sequence')])),
                ('notes', models.TextField(blank=True)),
                ('is_title_safe', models.NullBooleanField()),
                ('made_by', models.ForeignKey(related_name='assets_created', to=settings.AUTH_USER_MODEL)),
                ('owners', models.ManyToManyField(related_name='assets_owned', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'In Progress'), (100, b'Complete')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'asset', b'type', b'created'), blank=True, unique=True)),
                ('paid', models.BooleanField(default=False)),
                ('canceled', models.BooleanField(default=False)),
                ('fee', models.DecimalField(max_digits=20, decimal_places=2)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MakeDCPJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Requested'), (50, b'In Progress'), (100, b'Completed')])),
                ('two_d_to_3d', models.BooleanField(default=False, verbose_name=b'Make 2D version from 3D source')),
                ('four_k_to_2K_scaling', models.BooleanField(default=False, verbose_name=b'Make 2D version from 4K source')),
                ('foureight_fps_to_twofour_fps', models.BooleanField(default=False, verbose_name=b'Make 24 fps version from HFR source')),
                ('audio_adjustment_to_85dBs', models.BooleanField(default=False, verbose_name=b'Adjust loudness to 85Leq(M)')),
                ('number_of_copies', models.IntegerField(default=1, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('create_encrypted_dcp', models.BooleanField(default=False, verbose_name=b'Create Encrypted DCP')),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.CreateModel(
            name='OrderPhysicalDCPJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Requested'), (33, b'In Progress'), (66, b'Shipped'), (100, b'Received')])),
                ('two_d_to_3d', models.BooleanField(default=False, verbose_name=b'Make 2D version from 3D source')),
                ('four_k_to_2K_scaling', models.BooleanField(default=False, verbose_name=b'Make 2D version from 4K source')),
                ('foureight_fps_to_twofour_fps', models.BooleanField(default=False, verbose_name=b'Make 24 fps version from HFR source')),
                ('audio_adjustment_to_85dBs', models.BooleanField(default=False, verbose_name=b'Adjust loudness to 85Leq(M)')),
                ('create_encrypted_dcp', models.BooleanField(default=False, verbose_name=b'Create Encrypted DCP')),
                ('number_of_copies', models.IntegerField(default=1, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.CreateModel(
            name='RequestQCCheckJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Fail'), (1, b'Requested'), (33, b'Scheduled'), (66, b'In Progress'), (100, b'Pass')])),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.CreateModel(
            name='SendBlurayJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Requested'), (33, b'In Progress'), (66, b'Shipped'), (100, b'Received')])),
                ('addresses', models.ManyToManyField(to='user_manager.Address')),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.CreateModel(
            name='SendDCPJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Requested'), (50, b'In Progress'), (100, b'Completed')])),
                ('screening_start_date', models.DateField()),
                ('screening_end_date', models.DateField()),
                ('addresses', models.ManyToManyField(to='user_manager.ScreeningRoom')),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.CreateModel(
            name='SendDVDJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Requested'), (33, b'In Progress'), (66, b'Shipped'), (100, b'Received')])),
                ('video_format', models.CharField(default=b'NTSC', max_length=10, choices=[(b'NTSC', b'NTSC'), (b'PAL', b'PAL')])),
                ('addresses', models.ManyToManyField(to='user_manager.Address')),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.CreateModel(
            name='ShippingJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Canceled'), (1, b'Entered'), (50, b'In Transit'), (100, b'Delivered')])),
                ('fedex_tracking', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.AddField(
            model_name='job',
            name='asset',
            field=models.ForeignKey(to='asset_portal.Asset'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='invoice',
            field=models.ForeignKey(blank=True, to='user_manager.Invoice', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='made_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='owners',
            field=models.ManyToManyField(related_name='+', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='job',
            field=models.ForeignKey(to='asset_portal.SendDCPJob'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='screening_room',
            field=models.ForeignKey(to='user_manager.ScreeningRoom'),
            preserve_default=True,
        ),
    ]
