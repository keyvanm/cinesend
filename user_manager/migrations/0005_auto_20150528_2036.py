# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0004_auto_20150519_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screeningroom',
            name='screen_size',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
