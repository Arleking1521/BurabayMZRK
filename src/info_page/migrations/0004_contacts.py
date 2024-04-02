# Generated by Django 5.0.2 on 2024-03-21 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_page', '0003_managers_reception'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title')),
                ('info', models.TextField(verbose_name='Information')),
            ],
        ),
    ]