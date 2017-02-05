# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 15:40
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion_Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=50), unique=True)),
            ],
            options={
                'db_table': 'suggestion_types',
                'ordering': ('slug',),
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='Suggestion_Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('name', models.CharField(max_length=60)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=60, populate_from=models.CharField(max_length=60), unique=True)),
            ],
            options={
                'db_table': 'suggestion_sub_types',
            },
        ),
        migrations.AlterUniqueTogether(
            name='suggestion_sub_category',
            unique_together=set([('category_id', 'sub_category_id')]),
        ),
    ]
