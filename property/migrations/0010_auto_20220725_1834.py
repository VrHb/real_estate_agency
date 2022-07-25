# Generated by Django 2.2.24 on 2022-07-25 15:34

from django.db import migrations

import phonenumbers


def parse_owner_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        phone_number = flat.owners_phonenumber
        flat.owner_pure_phone = phonenumbers.parse(phone_number)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20220725_1828'),
    ]

    operations = [
        migrations.RunPython(parse_owner_phonenumbers)
    ]
