# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitor',
            name='chain',
            field=models.CharField(blank=True, max_length=100, choices=[(b'Cineplex', b'Cineplex')]),
            preserve_default=True,
        ),
    ]
