# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-13 13:59
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets_manager', '0009_auto_20170405_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='checksum',
            field=models.CharField(db_index=True, editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='asset',
            name='filename',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='type',
            field=models.CharField(blank=True, db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='assetbucket',
            name='name',
            field=models.CharField(db_index=True, default='UNKNOW', max_length=256, unique=True, verbose_name='nome'),
        ),
    ]
