# Generated by Django 4.2.1 on 2024-06-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0016_remove_reservation_is_favorite_dish_is_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Women',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='title',
        ),
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='name',
            field=models.CharField(default='Unnamed Dish', max_length=100),
        ),
        migrations.AddField(
            model_name='dish',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='dish',
            name='reviews_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
