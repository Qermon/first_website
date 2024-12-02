from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Review(models.Model):
    message = models.TextField()
    image = models.ImageField(upload_to='reviews/', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='reviews', null=True)
    RATING_CHOICES = (
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self):
        return self.message[:50]


class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner')
    ]

    name = models.CharField(max_length=100, default='Unnamed Dish')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    reviews_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Favorites(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    reviews_count = models.IntegerField(default=0)

    def __str__(self):
        return f'Favorites for {self.user.username} | Dish {self.name}'


class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    table_number = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return f"Reservation for {self.user} on {self.date} at {self.time}, Table {self.table_number}"


