# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import livefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0004_dcp_container'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcp',
            name='live',
            field=livefield.fields.LiveField(default=True),
            preserve_default=True,
        ),
    ]
