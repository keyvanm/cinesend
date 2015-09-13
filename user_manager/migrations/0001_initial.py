# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('type', models.CharField(default=b'shipping', max_length=20, choices=[(b'billing', b'billing'), (b'shipping', b'shipping')])),
                ('privacy', models.CharField(default=b'private', max_length=20, choices=[(b'private', b'Private'), (b'pending', b'Pending Approval'), (b'public', b'Public')])),
                ('primary', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200, blank=True)),
                ('company_name', models.CharField(max_length=255, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('address1', models.CharField(max_length=255, verbose_name=b'Street Address')),
                ('address2', models.CharField(max_length=255, verbose_name=b'Apt/Suite/Bldg', blank=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200, verbose_name=b'State/Province')),
                ('postal_code', models.CharField(max_length=20, verbose_name=b'ZIP/Postal Code')),
                ('country', models.CharField(max_length=200)),
                ('user', models.ForeignKey(related_name='personal_addresses', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_id', models.CharField(max_length=50)),
                ('fingerprint', models.CharField(max_length=50)),
                ('user', models.ForeignKey(related_name='creditcards', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exhibitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approved', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('chain', models.CharField(max_length=100, blank=True)),
                ('address', models.OneToOneField(to='user_manager.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('paid_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50, choices=[(b'RESELLER', b'Reseller'), (b'DIST', b'Distributor')])),
                ('credit', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScreeningRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encryption', models.TextField()),
                ('room_number', models.CharField(max_length=100)),
                ('three_dimension_support', models.BooleanField(default=False)),
                ('closed_caption_support', models.BooleanField(default=False)),
                ('described_service_support', models.BooleanField(default=False)),
                ('imax_support', models.BooleanField(default=False)),
                ('atmos_support', models.BooleanField(default=False)),
                ('dolby_seven_support', models.BooleanField(default=False)),
                ('capacity', models.IntegerField(null=True, blank=True)),
                ('screen_size', models.DecimalField(max_digits=10, decimal_places=2)),
                ('four_k_support', models.BooleanField(default=False)),
                ('hfr_support', models.BooleanField(default=False)),
                ('dbox_support', models.BooleanField(default=False)),
                ('exhibitor', models.ForeignKey(to='user_manager.Exhibitor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, blank=True)),
                ('stripe_customer_id', models.CharField(max_length=50, blank=True)),
                ('org', models.ForeignKey(blank=True, to='user_manager.Organization', null=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='festival',
            name='organization',
            field=models.ForeignKey(blank=True, to='user_manager.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='festival',
            name='print_traffic_address',
            field=models.OneToOneField(related_name='festival_print_traffic', to='user_manager.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='festival',
            name='submission_address',
            field=models.OneToOneField(related_name='festival_submission', to='user_manager.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='organization',
            field=models.ForeignKey(blank=True, to='user_manager.Organization', null=True),
            preserve_default=True,
        ),
    ]
