# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file_type',
            field=models.CharField(blank=True, max_length=50, choices=[(b'ProRes 4444', b'ProRes 4444'), (b'ProRes 422HQ', b'ProRes 422HQ'), (b'DNxHD', b'DNxHD'), (b'TIFF Sequence', b'TIFF Sequence'), (b'DPX Sequence', b'DPX Sequence')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset',
            name='source_colorspace',
            field=models.CharField(max_length=50, choices=[(b'UNKNOWN', b"I'm not sure"), (b'REC_709', b'Rec.709'), (b'DCI', b'DCI P3')]),
            preserve_default=True,
        ),
    ]
