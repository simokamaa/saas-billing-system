# Generated by Django 4.2.1 on 2023-08-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
