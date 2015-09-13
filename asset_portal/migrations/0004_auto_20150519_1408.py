# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0009_auto_20150519_1400'),
        ('asset_portal', '0003_auto_20150518_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendblurayjob',
            name='bluray',
            field=models.ForeignKey(default=1, to='vault.Bluray'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='senddvdjob',
            name='dvd',
            field=models.ForeignKey(default=1, to='vault.DVD'),
            preserve_default=False,
        ),
    ]
