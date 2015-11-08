# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=256)),
                ('link', models.URLField(verbose_name='Link', max_length=256)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('time_was_add', models.DateTimeField(verbose_name='Time add', auto_now_add=True)),
                ('votes_pros', models.IntegerField(verbose_name='Likes for', default=0)),
                ('votes_cons', models.IntegerField(verbose_name='Likes against', default=0)),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
    ]
