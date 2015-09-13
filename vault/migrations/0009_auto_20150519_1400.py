# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_portal', '0003_auto_20150518_1505'),
        ('vault', '0008_auto_20150514_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='bluray',
            name='job',
            field=models.ForeignKey(default=1, to='asset_portal.EncodeBlurayJob'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dvd',
            name='job',
            field=models.ForeignKey(default=1, to='asset_portal.EncodeDVDJob'),
            preserve_default=False,
        ),
    ]
