# Generated by Django 5.0.2 on 2024-03-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_page', '0002_managers_alter_pacientinfo_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='reception',
            field=models.TextField(default='none', verbose_name='Day and time of reception'),
        ),
    ]
