# Generated by Django 3.2.3 on 2021-06-24 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20210617_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='infection',
            name='date_string',
            field=models.CharField(default='no_value', max_length=100),
        ),
    ]
