# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161025_0658'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='dire',
            field=models.TextField(default='Throw it together and hope for the best.'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='favorites',
            field=models.ManyToManyField(related_name='favs', to='login.User'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='isprivate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='desc',
            field=models.TextField(default='No discription entered.'),
        ),
    ]
