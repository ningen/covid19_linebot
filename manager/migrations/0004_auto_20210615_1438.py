# Generated by Django 3.2.3 on 2021-06-15 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20210615_1428'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
    ]
