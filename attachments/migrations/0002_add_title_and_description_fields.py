# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import attachments.models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='description',
            field=models.TextField(default='', max_length=1000, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='attachment',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment_file',
            field=models.FileField(upload_to=attachments.models.attachment_upload, max_length=200, verbose_name='attachment'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='creator',
            field=models.ForeignKey(related_name='created_attachments', on_delete=models.SET(1), verbose_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
