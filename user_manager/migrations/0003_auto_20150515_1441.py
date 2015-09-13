# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_auto_20150512_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='screeningroom',
            name='media_block_model',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screeningroom',
            name='media_block_serial_number',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screeningroom',
            name='projector_model',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screeningroom',
            name='projector_serial_number',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exhibitor',
            name='chain',
            field=models.CharField(blank=True, max_length=100, choices=[(b'Cineplex', b'Cineplex'), (b'Alliance Cinemas', b'Alliance Cinemas'), (b'Cine Enterprise', b'Cine Enterprise'), (b'Cinema Guzzo', b'Cinema Guzzo'), (b'CineStarz', b'CineStarz'), (b'Criterion', b'Criterion'), (b'Golden', b'Golden'), (b'Hollywood 3', b'Hollywood 3'), (b'Imagine Cinemas', b'Imagine Cinemas'), (b'Landmark Cinemas', b'Landmark Cinemas'), (b'Magic Lantern Theatres', b'Magic Lantern Theatres'), (b'May', b'May'), (b'OTG Cinemas', b'OTG Cinemas'), (b'Rainbow Cinemas', b'Rainbow Cinemas'), (b'RGFM', b'RGFM')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='atmos_support',
            field=models.BooleanField(default=False, verbose_name=b'ATMOS'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='capacity',
            field=models.IntegerField(null=True, verbose_name=b'Seating Capacity', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='closed_caption_support',
            field=models.BooleanField(default=False, verbose_name=b'CC'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='dbox_support',
            field=models.BooleanField(default=False, verbose_name=b'DBOX'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='described_service_support',
            field=models.BooleanField(default=False, verbose_name=b'DS'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='dolby_seven_support',
            field=models.BooleanField(default=False, verbose_name=b'7.1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='four_k_support',
            field=models.BooleanField(default=False, verbose_name=b'4K'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='hfr_support',
            field=models.BooleanField(default=False, verbose_name=b'HFR'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='imax_support',
            field=models.BooleanField(default=False, verbose_name=b'IMAX'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screeningroom',
            name='three_dimension_support',
            field=models.BooleanField(default=False, verbose_name=b'3D'),
            preserve_default=True,
        ),
    ]
