# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bleachingrecord',
            name='firstly_created',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='greignyarnrecord',
            name='firstly_created',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='paintingrecord',
            name='firstly_created',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='postprocessingrecord',
            name='firstly_created',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='printingrecord',
            name='firstly_created',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='weavingrecord',
            name='firstly_created',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='windingrecord',
            name='firstly_created',
            field=models.BooleanField(default=True),
        ),
    ]
