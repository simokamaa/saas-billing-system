# Generated by Django 4.2.4 on 2023-08-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_payment_gateway_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='router',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('client_name', models.CharField(max_length=255)),
                ('ip_adressv4', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('start_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='router_hotspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('area_name', models.CharField(max_length=255)),
                ('ip_adressv4', models.FloatField()),
                ('start_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]