# Generated by Django 5.0.2 on 2024-03-21 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_page', '0004_contacts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Managers',
        ),
    ]
