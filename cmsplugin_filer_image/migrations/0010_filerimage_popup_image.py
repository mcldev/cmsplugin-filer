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
            field=models.BooleanField(default=True, verbose_name='Popup original image on click (disables links)'),
        ),
    ]
