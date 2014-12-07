# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comienso', '0004_auto_20141204_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='pais',
        ),
    ]
