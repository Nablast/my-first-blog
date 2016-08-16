# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160709_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nom')),
                ('quantity', models.IntegerField(blank=True, default=1, verbose_name='Quantite')),
                ('isDone', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ShopList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nom')),
                ('isDone', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastmaj_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('peopleGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopLists', to='blog.PeopleGroup')),
            ],
        ),
        migrations.RenameField(
            model_name='person',
            old_name='person',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='person',
            name='peopleGroup',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='blog.PeopleGroup'),
        ),
        migrations.AddField(
            model_name='item',
            name='shopLists',
            field=models.ManyToManyField(blank=True, related_name='items', to='blog.ShopList'),
        ),
    ]