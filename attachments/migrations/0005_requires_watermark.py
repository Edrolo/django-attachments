# Generated by Django 3.0.8 on 2020-07-15 06:39

from django.db import migrations, models
import attachments.models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0004_change_model_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='requires_watermark',
            field=models.BooleanField(null=True, verbose_name='Requires Watermark'),
        ),
    ]