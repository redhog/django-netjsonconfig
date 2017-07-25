# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0030_device_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='backend',
            field=models.CharField(choices=[('netjsonconfig.OpenWrt', 'OpenWRT/LEDE'), ('netjsonconfig.OpenWisp', 'OpenWISP Firmware 1.x'), ('netjsonconfig.Raspbian', 'Raspbian Jessie')], help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend', max_length=128, verbose_name='backend'),
        ),
        migrations.AlterField(
            model_name='template',
            name='backend',
            field=models.CharField(choices=[('netjsonconfig.OpenWrt', 'OpenWRT/LEDE'), ('netjsonconfig.OpenWisp', 'OpenWISP Firmware 1.x'), ('netjsonconfig.Raspbian', 'Raspbian Jessie')], help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend', max_length=128, verbose_name='backend'),
        ),
    ]
