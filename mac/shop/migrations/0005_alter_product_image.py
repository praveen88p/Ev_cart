# Generated by Django 4.1.3 on 2023-01-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='smac\\media\\shop\\images'),
        ),
    ]
