# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20170325_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='newtable',
            name='text_f',
            field=models.TextField(null=True, verbose_name='\u7528\u5728HTML\u8868\u55ae'),
        ),
    ]
