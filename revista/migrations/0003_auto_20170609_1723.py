# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0002_auto_20170609_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='validade',
            field=models.DateTimeField(),
        ),
    ]
