# Generated by Django 2.2.24 on 2022-07-25 16:40

from django.db import migrations

import phonenumbers


def parse_owner_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        phone_number = flat.owners_phonenumber
        flat.owner_pure_number = phonenumbers.parse(phone_number, "RU")
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220725_1858'),
    ]

    operations = [
        migrations.RunPython(parse_owner_phonenumbers)
    ]