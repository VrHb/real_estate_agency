# Generated by Django 2.2.24 on 2022-08-23 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220823_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='text',
            field=models.TextField(verbose_name='Текст заявки'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='who_appeal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
