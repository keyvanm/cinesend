# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bluray',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('running_time', durationfield.db.models.fields.duration.DurationField()),
                ('frame_rate', models.CharField(max_length=50, choices=[(b'24', b'24 fps'), (b'25', b'25 fps'), (b'30', b'30 fps'), (b'48', b'48 fps'), (b'50', b'50 fps'), (b'60', b'60 fps')])),
                ('aspect_ratio', models.CharField(max_length=50, choices=[(b'43', b'4:3'), (b'169', b'16:9')])),
                ('audio_track_1', models.CharField(max_length=50, choices=[(b'2Discreet', b'2.0 Discreet'), (b'51Discreet', b'5.1 Discreet'), (b'51Dolby', b'5.1 Dolby Prologic II'), (b'51DTS', b'5.1 DTS')])),
                ('audio_track_2', models.CharField(blank=True, max_length=50, choices=[(b'2Discreet', b'2.0 Discreet'), (b'51Discreet', b'5.1 Discreet'), (b'51Dolby', b'5.1 Dolby Prologic II'), (b'51DTS', b'5.1 DTS')])),
                ('audio_language', models.CharField(max_length=50, choices=[(b'SQ', b'SQ - ALBANIAN'), (b'AR', b'AR - ARABIC'), (b'BS', b'BS - BOSNIAN'), (b'BG', b'BG - BULGARIAN'), (b'CA', b'CA - CATALAN'), (b'YUE', b'YUE - CHINESE - CANTONESE'), (b'HR', b'HR - CROATIAN'), (b'CS', b'CS - CZECH'), (b'DA', b'DA - DANISH'), (b'NL', b'NL - DUTCH'), (b'EN', b'EN - ENGLISH'), (b'ET', b'ET - ESTONIAN'), (b'EU', b'EU - EUSKARA'), (b'FI', b'FI - FINNISH'), (b'VLS', b'VLS - FLEMISH'), (b'FR', b'FR - FRENCH'), (b'QFC', b'QFC - FRENCH - CANADIAN'), (b'DE', b'DE - GERMAN'), (b'GSW', b'GSW - GERMAN - SWISS'), (b'EL', b'EL - GREEK'), (b'HE', b'HE - HEBREW'), (b'HI', b'HI - HINDI'), (b'HU', b'HU - HUNGARIAN'), (b'IS', b'IS - ICELANDIC'), (b'IND', b'IND - INDONESIAN BAHASA'), (b'IT', b'IT - ITALIAN'), (b'JA', b'JA - JAPANESE'), (b'KK', b'KK - KAZAKH'), (b'KO', b'KO - KOREAN'), (b'LV', b'LV - LATVIAN'), (b'LT', b'LT - LITHUANIAN'), (b'MSA', b'MSA - MALAY BAHASA'), (b'MN', b'MN - MONGOLIAN'), (b'NO', b'NO - NORWEGIAN'), (b'PL', b'PL - POLISH'), (b'QBP', b'QBP - PORTUGUESE - BRAZILIAN'), (b'PT', b'PT - PORTUGUESE - EUROPEAN'), (b'RO', b'RO - ROMANIAN'), (b'RU', b'RU - RUSSIAN'), (b'SR', b'SR - SERBIAN'), (b'SK', b'SK - SLOVAK'), (b'SL', b'SL - SLOVENIAN'), (b'QSA', b'QSA - SPANISH - ARGENTINIAN'), (b'ES', b'ES - SPANISH - CASTILIAN'), (b'LAS', b'LAS - SPANISH - LATIN AMERICAN'), (b'QSM', b'QSM - SPANISH - MEXICAN'), (b'SV', b'SV - SWEDISH'), (b'TA', b'TA - TAMIL'), (b'TE', b'TE - TELUGU'), (b'TH', b'TH - THAI'), (b'TR', b'TR - TURKISH'), (b'UK', b'UK - UKRAINIAN'), (b'VI', b'VI - VIETNAMESE'), (b'WEL', b'WEL - WELSH (CYMRU)'), (b'NAN', b'NAN - CHINESE - TAIWANESE (Audio Only)'), (b'QTM', b'QTM - CHINESE - TAIWANESE MANDARIN (Audio Only)'), (b'CMN', b'CMN - CHINESE - MANDARIN PRC (Audio Only)'), (b'XX', b'XX - NO SPOKEN LANGUAGE')])),
                ('subtitle_language', models.CharField(max_length=50, choices=[(b'SQ', b'SQ - ALBANIAN'), (b'AR', b'AR - ARABIC'), (b'BS', b'BS - BOSNIAN'), (b'BG', b'BG - BULGARIAN'), (b'CA', b'CA - CATALAN'), (b'YUE', b'YUE - CHINESE - CANTONESE'), (b'HR', b'HR - CROATIAN'), (b'CS', b'CS - CZECH'), (b'DA', b'DA - DANISH'), (b'NL', b'NL - DUTCH'), (b'EN', b'EN - ENGLISH'), (b'ET', b'ET - ESTONIAN'), (b'EU', b'EU - EUSKARA'), (b'FI', b'FI - FINNISH'), (b'VLS', b'VLS - FLEMISH'), (b'FR', b'FR - FRENCH'), (b'QFC', b'QFC - FRENCH - CANADIAN'), (b'DE', b'DE - GERMAN'), (b'GSW', b'GSW - GERMAN - SWISS'), (b'EL', b'EL - GREEK'), (b'HE', b'HE - HEBREW'), (b'HI', b'HI - HINDI'), (b'HU', b'HU - HUNGARIAN'), (b'IS', b'IS - ICELANDIC'), (b'IND', b'IND - INDONESIAN BAHASA'), (b'IT', b'IT - ITALIAN'), (b'JA', b'JA - JAPANESE'), (b'KK', b'KK - KAZAKH'), (b'KO', b'KO - KOREAN'), (b'LV', b'LV - LATVIAN'), (b'LT', b'LT - LITHUANIAN'), (b'MSA', b'MSA - MALAY BAHASA'), (b'MN', b'MN - MONGOLIAN'), (b'NO', b'NO - NORWEGIAN'), (b'PL', b'PL - POLISH'), (b'QBP', b'QBP - PORTUGUESE - BRAZILIAN'), (b'PT', b'PT - PORTUGUESE - EUROPEAN'), (b'RO', b'RO - ROMANIAN'), (b'RU', b'RU - RUSSIAN'), (b'SR', b'SR - SERBIAN'), (b'SK', b'SK - SLOVAK'), (b'SL', b'SL - SLOVENIAN'), (b'QSA', b'QSA - SPANISH - ARGENTINIAN'), (b'ES', b'ES - SPANISH - CASTILIAN'), (b'LAS', b'LAS - SPANISH - LATIN AMERICAN'), (b'QSM', b'QSM - SPANISH - MEXICAN'), (b'SV', b'SV - SWEDISH'), (b'TA', b'TA - TAMIL'), (b'TE', b'TE - TELUGU'), (b'TH', b'TH - THAI'), (b'TR', b'TR - TURKISH'), (b'UK', b'UK - UKRAINIAN'), (b'VI', b'VI - VIETNAMESE'), (b'WEL', b'WEL - WELSH (CYMRU)'), (b'QMS', b'QMS - CHINESE - MANDARIN SIMPLIFIED (Subtitles Only)'), (b'QMT', b'QMT - CHINESE - MANDARIN TRADITIONAL (Subtitles Only)'), (b'XX', b'XX - NO SUBTITLE')])),
                ('subtitle_type', models.CharField(max_length=50, choices=[(b'burnin', b'Burn-in'), (b'external', b'External')])),
                ('letterboxed', models.BooleanField(default=False)),
                ('pillarboxed', models.BooleanField(default=False)),
                ('encoding', models.CharField(max_length=50, choices=[(b'mpeg2', b'MPEG 2'), (b'h264', b'H.264')])),
                ('resolution', models.CharField(max_length=50, choices=[(b'720p', b'720p'), (b'1080p', b'1080p')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('running_time', durationfield.db.models.fields.duration.DurationField()),
                ('frame_rate', models.CharField(max_length=50, choices=[(b'24', b'24 fps'), (b'25', b'25 fps'), (b'30', b'30 fps'), (b'48', b'48 fps'), (b'50', b'50 fps'), (b'60', b'60 fps')])),
                ('aspect_ratio', models.CharField(max_length=50, choices=[(b'43', b'4:3'), (b'169', b'16:9')])),
                ('audio_track_1', models.CharField(max_length=50, choices=[(b'2Discreet', b'2.0 Discreet'), (b'51Discreet', b'5.1 Discreet'), (b'51Dolby', b'5.1 Dolby Prologic II'), (b'51DTS', b'5.1 DTS')])),
                ('audio_track_2', models.CharField(blank=True, max_length=50, choices=[(b'2Discreet', b'2.0 Discreet'), (b'51Discreet', b'5.1 Discreet'), (b'51Dolby', b'5.1 Dolby Prologic II'), (b'51DTS', b'5.1 DTS')])),
                ('audio_language', models.CharField(max_length=50, choices=[(b'SQ', b'SQ - ALBANIAN'), (b'AR', b'AR - ARABIC'), (b'BS', b'BS - BOSNIAN'), (b'BG', b'BG - BULGARIAN'), (b'CA', b'CA - CATALAN'), (b'YUE', b'YUE - CHINESE - CANTONESE'), (b'HR', b'HR - CROATIAN'), (b'CS', b'CS - CZECH'), (b'DA', b'DA - DANISH'), (b'NL', b'NL - DUTCH'), (b'EN', b'EN - ENGLISH'), (b'ET', b'ET - ESTONIAN'), (b'EU', b'EU - EUSKARA'), (b'FI', b'FI - FINNISH'), (b'VLS', b'VLS - FLEMISH'), (b'FR', b'FR - FRENCH'), (b'QFC', b'QFC - FRENCH - CANADIAN'), (b'DE', b'DE - GERMAN'), (b'GSW', b'GSW - GERMAN - SWISS'), (b'EL', b'EL - GREEK'), (b'HE', b'HE - HEBREW'), (b'HI', b'HI - HINDI'), (b'HU', b'HU - HUNGARIAN'), (b'IS', b'IS - ICELANDIC'), (b'IND', b'IND - INDONESIAN BAHASA'), (b'IT', b'IT - ITALIAN'), (b'JA', b'JA - JAPANESE'), (b'KK', b'KK - KAZAKH'), (b'KO', b'KO - KOREAN'), (b'LV', b'LV - LATVIAN'), (b'LT', b'LT - LITHUANIAN'), (b'MSA', b'MSA - MALAY BAHASA'), (b'MN', b'MN - MONGOLIAN'), (b'NO', b'NO - NORWEGIAN'), (b'PL', b'PL - POLISH'), (b'QBP', b'QBP - PORTUGUESE - BRAZILIAN'), (b'PT', b'PT - PORTUGUESE - EUROPEAN'), (b'RO', b'RO - ROMANIAN'), (b'RU', b'RU - RUSSIAN'), (b'SR', b'SR - SERBIAN'), (b'SK', b'SK - SLOVAK'), (b'SL', b'SL - SLOVENIAN'), (b'QSA', b'QSA - SPANISH - ARGENTINIAN'), (b'ES', b'ES - SPANISH - CASTILIAN'), (b'LAS', b'LAS - SPANISH - LATIN AMERICAN'), (b'QSM', b'QSM - SPANISH - MEXICAN'), (b'SV', b'SV - SWEDISH'), (b'TA', b'TA - TAMIL'), (b'TE', b'TE - TELUGU'), (b'TH', b'TH - THAI'), (b'TR', b'TR - TURKISH'), (b'UK', b'UK - UKRAINIAN'), (b'VI', b'VI - VIETNAMESE'), (b'WEL', b'WEL - WELSH (CYMRU)'), (b'NAN', b'NAN - CHINESE - TAIWANESE (Audio Only)'), (b'QTM', b'QTM - CHINESE - TAIWANESE MANDARIN (Audio Only)'), (b'CMN', b'CMN - CHINESE - MANDARIN PRC (Audio Only)'), (b'XX', b'XX - NO SPOKEN LANGUAGE')])),
                ('subtitle_language', models.CharField(max_length=50, choices=[(b'SQ', b'SQ - ALBANIAN'), (b'AR', b'AR - ARABIC'), (b'BS', b'BS - BOSNIAN'), (b'BG', b'BG - BULGARIAN'), (b'CA', b'CA - CATALAN'), (b'YUE', b'YUE - CHINESE - CANTONESE'), (b'HR', b'HR - CROATIAN'), (b'CS', b'CS - CZECH'), (b'DA', b'DA - DANISH'), (b'NL', b'NL - DUTCH'), (b'EN', b'EN - ENGLISH'), (b'ET', b'ET - ESTONIAN'), (b'EU', b'EU - EUSKARA'), (b'FI', b'FI - FINNISH'), (b'VLS', b'VLS - FLEMISH'), (b'FR', b'FR - FRENCH'), (b'QFC', b'QFC - FRENCH - CANADIAN'), (b'DE', b'DE - GERMAN'), (b'GSW', b'GSW - GERMAN - SWISS'), (b'EL', b'EL - GREEK'), (b'HE', b'HE - HEBREW'), (b'HI', b'HI - HINDI'), (b'HU', b'HU - HUNGARIAN'), (b'IS', b'IS - ICELANDIC'), (b'IND', b'IND - INDONESIAN BAHASA'), (b'IT', b'IT - ITALIAN'), (b'JA', b'JA - JAPANESE'), (b'KK', b'KK - KAZAKH'), (b'KO', b'KO - KOREAN'), (b'LV', b'LV - LATVIAN'), (b'LT', b'LT - LITHUANIAN'), (b'MSA', b'MSA - MALAY BAHASA'), (b'MN', b'MN - MONGOLIAN'), (b'NO', b'NO - NORWEGIAN'), (b'PL', b'PL - POLISH'), (b'QBP', b'QBP - PORTUGUESE - BRAZILIAN'), (b'PT', b'PT - PORTUGUESE - EUROPEAN'), (b'RO', b'RO - ROMANIAN'), (b'RU', b'RU - RUSSIAN'), (b'SR', b'SR - SERBIAN'), (b'SK', b'SK - SLOVAK'), (b'SL', b'SL - SLOVENIAN'), (b'QSA', b'QSA - SPANISH - ARGENTINIAN'), (b'ES', b'ES - SPANISH - CASTILIAN'), (b'LAS', b'LAS - SPANISH - LATIN AMERICAN'), (b'QSM', b'QSM - SPANISH - MEXICAN'), (b'SV', b'SV - SWEDISH'), (b'TA', b'TA - TAMIL'), (b'TE', b'TE - TELUGU'), (b'TH', b'TH - THAI'), (b'TR', b'TR - TURKISH'), (b'UK', b'UK - UKRAINIAN'), (b'VI', b'VI - VIETNAMESE'), (b'WEL', b'WEL - WELSH (CYMRU)'), (b'QMS', b'QMS - CHINESE - MANDARIN SIMPLIFIED (Subtitles Only)'), (b'QMT', b'QMT - CHINESE - MANDARIN TRADITIONAL (Subtitles Only)'), (b'XX', b'XX - NO SUBTITLE')])),
                ('subtitle_type', models.CharField(max_length=50, choices=[(b'burnin', b'Burn-in'), (b'external', b'External')])),
                ('letterboxed', models.BooleanField(default=False)),
                ('pillarboxed', models.BooleanField(default=False)),
                ('region', models.CharField(max_length=50, choices=[(b'ntsc', b'NTSC'), (b'pal', b'PAL')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
