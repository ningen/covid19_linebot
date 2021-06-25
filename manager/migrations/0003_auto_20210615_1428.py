# Generated by Django 3.2.3 on 2021-06-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_posts_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
