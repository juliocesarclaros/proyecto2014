# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comienso', '0003_auto_20141125_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='partidas_jugadas',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='perfil',
            name='puntaje_total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
