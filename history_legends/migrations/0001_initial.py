# Generated by Django 5.0.2 on 2024-03-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Title')),
                ('info', models.TextField(verbose_name='Information')),
            ],
        ),
    ]
