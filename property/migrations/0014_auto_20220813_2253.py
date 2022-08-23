# Generated by Django 2.2.24 on 2022-08-13 19:53

from textwrap import fill
from django.db import migrations


def fill_flats_in_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners.iterator():
        finded_flats = Flat.objects.filter(owner=owner.name)
        owner.flats.set(finded_flats)  # or maybe use owner.flats.add(finded_flats)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220813_2253'),
    ]

    operations = [
        migrations.RunPython(fill_flats_in_owners)
    ]
