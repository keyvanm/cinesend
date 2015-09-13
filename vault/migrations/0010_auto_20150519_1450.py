# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0009_auto_20150519_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bluray',
            name='job',
            field=models.OneToOneField(to='asset_portal.EncodeBlurayJob'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dcp',
            name='job',
            field=models.OneToOneField(to='asset_portal.MakeDCPJob'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dvd',
            name='job',
            field=models.OneToOneField(to='asset_portal.EncodeDVDJob'),
            preserve_default=True,
        ),
    ]
