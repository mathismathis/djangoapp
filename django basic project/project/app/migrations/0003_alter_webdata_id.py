# Generated by Django 3.2.7 on 2021-10-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211003_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]