# Generated by Django 3.2 on 2022-04-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidayapp', '0007_alter_apartmentprice_apartment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]