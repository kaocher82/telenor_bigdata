# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-01 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_delete_facttabledemo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactTableDemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.CharField(blank=True, max_length=255, null=True)),
                ('subscription_on', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_on', models.CharField(blank=True, max_length=255, null=True)),
                ('event_time', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_completed_on', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('membership_no', models.CharField(blank=True, max_length=255, null=True)),
                ('previous_product_code', models.CharField(blank=True, max_length=255, null=True)),
                ('current_product_code', models.CharField(blank=True, max_length=255, null=True)),
                ('retailer_type', models.CharField(blank=True, max_length=255, null=True)),
                ('retailer_area', models.CharField(blank=True, max_length=255, null=True)),
                ('retailer_pos_code', models.CharField(blank=True, max_length=255, null=True)),
                ('subscription_status', models.CharField(blank=True, max_length=255, null=True)),
                ('user_type', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=255, null=True)),
                ('subscription_type', models.CharField(blank=True, max_length=255, null=True)),
                ('subscription_channel', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction_channel', models.CharField(blank=True, max_length=255, null=True)),
                ('user_type1', models.CharField(blank=True, max_length=255, null=True)),
                ('parent_membership_no', models.CharField(blank=True, max_length=255, null=True)),
                ('relationship_with_parent', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
