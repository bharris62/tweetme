# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-24 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
