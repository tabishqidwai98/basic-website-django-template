# Generated by Django 3.1.6 on 2021-03-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
