# Generated by Django 3.2 on 2022-04-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidayapp', '0006_rename_name_of_app_apartmentprice_apartment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentprice',
            name='apartment_name',
            field=models.CharField(choices=[('Tony', '80.00'), ('Matea', '80.00'), ('Martina', '120.00')], max_length=20),
        ),
    ]
