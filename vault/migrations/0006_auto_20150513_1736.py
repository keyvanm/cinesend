# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_portal', '0002_auto_20150507_1356'),
        ('vault', '0005_dcp_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='bluray',
            name='asset',
            field=models.ForeignKey(related_name='+', default=0, to='asset_portal.Asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dvd',
            name='asset',
            field=models.ForeignKey(related_name='+', default=0, to='asset_portal.Asset'),
            preserve_default=False,
        ),
    ]
