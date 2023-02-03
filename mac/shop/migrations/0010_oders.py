# Generated by Django 4.1.3 on 2023-01-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_name_contact_name_remove_contact_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oders',
            fields=[
                ('Oders_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=700)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('zip_code', models.CharField(default='', max_length=500)),
                ('phone', models.CharField(default='', max_length=70)),
            ],
        ),
    ]