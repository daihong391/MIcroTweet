# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='userName',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='userName',
        ),
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ForeignKey(to='twitter.Following', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='tweet',
            field=models.ForeignKey(to='twitter.Tweet', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='following',
            name='following',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
