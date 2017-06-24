# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        verbose_name='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=99)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('arquivo', models.FileField(upload_to='revistas/')),
            ],
        ),
    ]
