# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0002_add_title_and_description_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='show_in_standard_package',
            field=models.BooleanField(default=True, verbose_name='Show in standard package'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='show_to_students',
            field=models.BooleanField(default=True, verbose_name='Show to students'),
        ),
    ]
