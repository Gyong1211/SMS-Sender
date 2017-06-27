# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('recipient', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=45)),
                ('send_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]