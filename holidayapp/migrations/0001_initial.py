# Generated by Django 3.2 on 2022-04-04 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('apartment_name', models.CharField(choices=[('Tony', 'Tony Apartment for max4 people'), ('Matea', 'Matea apartment for max4 people'), ('Martina', 'Martina apartment for max6 people')], max_length=10, primary_key=True, serialize=False)),
                ('beds_nr', models.IntegerField()),
                ('guest_nr', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('image1', models.ImageField(upload_to='')),
            ],
        ),
    ]
