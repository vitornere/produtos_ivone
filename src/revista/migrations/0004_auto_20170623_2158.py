# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0003_auto_20170609_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
