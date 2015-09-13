# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0003_auto_20150512_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcp',
            name='container',
            field=models.CharField(default='2kflat', max_length=50, choices=[(b'2kflat', b'2K Flat'), (b'2kscope', b'2K Scope'), (b'4kflat', b'4K Flat'), (b'4kscope', b'4K Scope')]),
            preserve_default=False,
        ),
    ]
