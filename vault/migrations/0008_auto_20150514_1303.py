# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0007_auto_20150513_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='bluray',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bluray',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dvd',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dvd',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True),
            preserve_default=True,
        ),
    ]
