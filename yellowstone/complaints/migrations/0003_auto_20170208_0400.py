# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 04:00
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_auto_20170205_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='complaintsubcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=60, populate_from='name', unique=True),
        ),
    ]
