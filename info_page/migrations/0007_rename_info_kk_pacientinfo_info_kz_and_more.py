# Generated by Django 5.0.2 on 2024-03-29 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_page', '0006_pacientinfo_info_kk_pacientinfo_info_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pacientinfo',
            old_name='info_kk',
            new_name='info_kz',
        ),
        migrations.RenameField(
            model_name='pacientinfo',
            old_name='title_kk',
            new_name='title_kz',
        ),
    ]