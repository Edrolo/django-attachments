# Generated by Django 3.0.8 on 2020-07-15 06:39

from django.db import migrations, models
import attachments.models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0006_requires_watermark_assign_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='requires_watermark',
            field=models.BooleanField(null=False, default=False, verbose_name='Requires Watermark'),
        ),
    ]
