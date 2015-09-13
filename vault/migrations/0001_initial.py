# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import durationfield.db.models.fields.duration
import django.utils.timezone
import django.core.validators
import sizefield.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('asset_portal', '0002_auto_20150507_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='DCP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('version_name', models.CharField(default=b'Original', max_length=200)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'asset', b'version_name'), blank=True, unique=True)),
                ('dimension_properties', models.CharField(max_length=50, verbose_name=b'2D/3D', choices=[(b'2D', b'2D Content'), (b'3D', b'3D Content')])),
                ('file_size', sizefield.models.FileSizeField()),
                ('dcp_standard', models.CharField(max_length=20, choices=[(b'smpte', b'SMPTE'), (b'interop', b'Interop')])),
                ('frame_rate', models.CharField(max_length=50, choices=[(b'24', b'24 fps'), (b'25', b'25 fps'), (b'30', b'30 fps'), (b'48', b'48 fps'), (b'50', b'50 fps'), (b'60', b'60 fps')])),
                ('running_time', durationfield.db.models.fields.duration.DurationField()),
                ('credit_offset', durationfield.db.models.fields.duration.DurationField(null=True, blank=True)),
                ('pkl_name', models.CharField(max_length=255, verbose_name=b'PKL Name')),
                ('composition_name', models.CharField(max_length=255)),
                ('number_of_reels', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('issuer', models.CharField(default=b'bitcine', max_length=255, choices=[(b'bitcine', b'BitCine Technologies')])),
                ('subtitle_type', models.CharField(max_length=50, choices=[(b'burnin', b'Burn-in'), (b'smpte', b'SMPTE'), (b'interop', b'Interop')])),
                ('asset', models.ForeignKey(to='asset_portal.Asset')),
                ('job', models.ForeignKey(to='asset_portal.MakeDCPJob')),
            ],
            options={
                'verbose_name': 'DCP',
            },
            bases=(models.Model,),
        ),
    ]
