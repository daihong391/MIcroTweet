# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_remove_tweet_tweetid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='userName',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
