# Generated by Django 4.2.1 on 2024-06-14 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0018_women'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='description',
        ),
    ]
