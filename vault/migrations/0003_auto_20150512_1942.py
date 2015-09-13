# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0002_bluray_dvd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcp',
            name='subtitle_type',
            field=models.CharField(blank=True, max_length=50, choices=[(b'burnin', b'Burn-in'), (b'smpte', b'SMPTE'), (b'interop', b'Interop')]),
            preserve_default=True,
        ),
    ]
