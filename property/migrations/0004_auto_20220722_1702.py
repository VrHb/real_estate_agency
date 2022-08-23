# Generated by Django 2.2.24 on 2022-07-22 14:02

from django.db import migrations


def fill_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    new_buildings = Flat.objects.filter(construction_year__gt=2015)
    for building in new_buildings:
        building.new_building = True
        building.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20220722_1626'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_field)
    ]
