from django.contrib import admin

from women.models import Dish

# Register your models here.
from django.contrib import admin
from .models import Review, Dish, Favorites, Reservation


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'rating', 'message', 'image')
    list_display_links = ('id', 'author', 'rating')
    search_fields = ('author__username', 'message')
    list_filter = ('rating',)
    list_per_page = 25


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'rating', 'reviews_count', 'is_favorite')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category')
    list_filter = ('category', 'is_favorite')
    list_per_page = 25


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dish', 'image', 'price', 'reviews_count')
    list_display_links = ('id', 'user', 'dish')
    search_fields = ('user__username', 'dish__name')
    list_per_page = 25


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'time', 'table_number')
    list_display_links = ('id', 'user', 'date')
    search_fields = ('user__username', 'date', 'time')
    list_per_page = 25
