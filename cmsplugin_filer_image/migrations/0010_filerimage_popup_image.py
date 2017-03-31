# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0009_auto_20160713_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerimage',
            name='popup_image',
            field=models.BooleanField(default=True, verbose_name='Popup original image on click (cannot be used with links)'),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='caption_text',
            field=models.CharField(max_length=255, null=True, verbose_name='Caption Title', blank=True),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='description',
            field=models.TextField(null=True, verbose_name='Caption Text', blank=True),
        ),
    ]
