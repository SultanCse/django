# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_products_list_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_list',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
