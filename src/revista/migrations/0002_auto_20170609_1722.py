# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revista',
            old_name='data',
            new_name='validade',
        ),
    ]
