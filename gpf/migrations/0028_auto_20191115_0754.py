# Generated by Django 2.2.6 on 2019-11-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0027_auto_20191114_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='type',
            field=models.CharField(max_length=128, verbose_name='mail_type'),
        ),
    ]
