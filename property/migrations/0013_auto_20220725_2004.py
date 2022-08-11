# Generated by Django 2.2.24 on 2022-07-25 17:04

from django.db import migrations

import phonenumbers


def parse_owner_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        phone_number = flat.owners_phonenumber
        flat.owner_pure_number = phonenumbers.parse(phone_number, "RU")
        if phonenumbers.is_valid_number(flat.owner_pure_number):
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220725_1940'),
    ]

    operations = [
        migrations.RunPython(parse_owner_phonenumbers)
    ]