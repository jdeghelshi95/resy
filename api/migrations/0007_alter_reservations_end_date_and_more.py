# Generated by Django 4.1.1 on 2022-09-15 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_reservations_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='start_date',
            field=models.DateField(),
        ),
    ]
