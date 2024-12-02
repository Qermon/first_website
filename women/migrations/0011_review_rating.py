# Generated by Django 4.2.1 on 2024-06-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_alter_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')], default=1),
            preserve_default=False,
        ),
    ]
