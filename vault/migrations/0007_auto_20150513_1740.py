# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0006_auto_20150513_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='bluray',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'asset', b'title'), blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dvd',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'asset', b'title'), blank=True, unique=True),
            preserve_default=True,
        ),
    ]
