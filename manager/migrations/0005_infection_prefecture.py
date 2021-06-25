# Generated by Django 3.2.3 on 2021-06-15 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20210615_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='prefecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='infection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('infection', models.IntegerField()),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.prefecture')),
            ],
        ),
    ]
