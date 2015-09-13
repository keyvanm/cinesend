# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_portal', '0002_auto_20150507_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncodeBlurayJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Requested'), (50, b'In Progress'), (100, b'Finished')])),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.CreateModel(
            name='EncodeDVDJob',
            fields=[
                ('job_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='asset_portal.Job')),
                ('status', models.IntegerField(default=1, choices=[(0, b'Error'), (1, b'Requested'), (50, b'In Progress'), (100, b'Finished')])),
                ('video_format', models.CharField(default=b'NTSC', max_length=10, choices=[(b'NTSC', b'NTSC'), (b'PAL', b'PAL')])),
            ],
            options={
                'abstract': False,
            },
            bases=('asset_portal.job',),
        ),
        migrations.RemoveField(
            model_name='senddvdjob',
            name='video_format',
        ),
    ]
