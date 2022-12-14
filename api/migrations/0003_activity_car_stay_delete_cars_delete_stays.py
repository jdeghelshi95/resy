# Generated by Django 4.1.1 on 2022-09-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_type', models.CharField(choices=[('boat', 'boat tours'), ('atv', 'atv tours and rides'), ('horse', 'Horse Back Riding Guided Tours'), ('fish', 'guided fishing tours')], max_length=6)),
                ('total_price', models.IntegerField(default=0)),
                ('guest_quantity', models.IntegerField(default=1)),
                ('rate', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('rate', models.CharField(max_length=50)),
                ('car_type', models.CharField(choices=[('S', 'Small Sedan'), ('M', 'Medium CrossOver'), ('L', 'Large Suv')], default='M', max_length=1)),
                ('total_price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('guest', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('guest_amount', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('rate', models.CharField(max_length=200)),
                ('total_price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
        migrations.DeleteModel(
            name='Stays',
        ),
    ]
