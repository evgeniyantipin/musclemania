# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'categories',
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=0, max_digits=6)),
                ('description', models.TextField(blank=True)),
                ('categories', models.ManyToManyField(to='categories.Category')),
            ],
            options={
                'db_table': 'products',
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('parent_category', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'db_table': 'subcategories',
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
            bases=(models.Model,),
        ),
    ]
