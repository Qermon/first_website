import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sitewomen.settings")
import django

django.setup()

from women.models import Dish

dishes = [
    {
        'name': 'Morning Fresh',
        'category': 'breakfast',
        'price': 12.50,
        'rating': 4.3,
        'reviews_count': 15,
        'image': 'images/breakfast/brett-jordan-8xt8-HIFqc8-unsplash.jpg',
        'is_favorite': False,

    },
    {
        'name': 'Tooplate Soup',
        'category': 'lunch',
        'price': 24.50,
        'rating': 3.0,
        'reviews_count': 47,
        'image': 'images/lunch/farhad-ibrahimzade-MGKqxm6u2bc-unsplash.jpg',
        'is_favorite': False,

    },
    {
        'name': 'Premium Steak',
        'category': 'dinner',
        'price': 45.00,
        'rating': 3.0,
        'reviews_count': 19,
        'image': 'images/dinner/keriliwi-c3mFafsFz2w-unsplash.jpg',
        'is_favorite': False,
    },
    {
        'name': 'Seafood Set',
        'category': 'dinner',
        'price': 86.00,
        'rating': 3.0,
        'reviews_count': 25,
        'image': 'images/dinner/farhad-ibrahimzade-ZipYER3NLhY-unsplash.jpg',
        'is_favorite': False,

    },
    {
        'name': 'Burger Set',
        'category': 'breakfast',
        'price': 20.50,
        'rating': 4.3,
        'reviews_count': 81,
        'image': 'images/breakfast/louis-hansel-dphM2U1xq0U-unsplash.jpg',
        'is_favorite': False,

    },
    {
        'name': 'Healthy Soup',
        'category': 'lunch',
        'price': 34.20,
        'rating': 3.0,
        'reviews_count': 64,
        'image': 'images/lunch/farhad-ibrahimzade-D5c9ZciQy_I-unsplash.jpg',
        'is_favorite': False,

    },
    {
        'name': 'Dumplings',
        'category': 'lunch',
        'price': 54.50,
        'reviews_count': 50,
        'rating': 5,
        'image': "images/lunch/4044651.jpg"
    },
    {
        'name': 'Baked Creamy',
        'category': 'breakfast',
        'price': 16.50,
        'rating': 3.0,
        'reviews_count': 70,
        'image': "images/breakfast/lucas-swennen-1W_MyJSRLuQ-unsplash.jpg"
    },

    {
        'name': 'Kebab',
        'category': 'lunch',
        'price': 31.70,
        'reviews_count': 29,
        'rating': 4.1,
        'image': "images/lunch/13-10-20-6-1-640x427.jpg"
    },


    {
        'name': 'Salmon Set',
        'category': 'dinner',
        'price': 60.00,
        'rating': 3.0,
        'reviews_count': 74,
        'image': "images/dinner/farhad-ibrahimzade-isHUj3N0194-unsplash.jpg"
    },
    {
        'name': 'Bread Steak Set',
        'category': 'lunch',
        'price': 42.50,
        'rating': 3.0,
        'reviews_count': 15,
        'image': "images/lunch/louis-hansel-rheOvfxOlOA-unsplash.jpg"
    },
    {
        'name': 'Steak Set',
        'category': 'lunch',
        'price': 32.75,
        'rating': 4.2,
        'reviews_count': 38,
        'image': "images/lunch/louis-hansel-cH5IPjaAYyo-unsplash.jpg"
    },
    {
        'name': 'Fried Chicken',
        'category': 'breakfast',
        'price': 44.80,
        'rating': 4.7,
        'reviews_count': 26,
        'image': "images/breakfast/mustard.jpg"
    },
    {
        'name': 'Hot Pizza',
        'category': 'breakfast',
        'price': 24.20,
        'rating': 3.7,
        'reviews_count': 16,
        'image': "images/breakfast/Pizza.jpg"
    },
    {
        'name': 'Spaghetti',
        'category': 'breakfast',
        'price': 14.90,
        'rating': 4.3,
        'reviews_count': 46,
        'image': "images/breakfast/spaghetti.jpg"
    },
    {
        'name': 'Broccoli Pasta',
        'category': 'dinner',
        'price': 34.50,
        'rating': 5,
        'reviews_count': 26,
        'image': "images/dinner/Pasta.jpg"
    },
    {
        'name': 'Meat pie',
        'category': 'dinner',
        'price': 54.00,
        'rating': 4.9,
        'reviews_count': 28,
        'image': "images/dinner/pie.jpg"
    },
    {
        'name': 'Cheesy Chicken',
        'category': 'dinner',
        'price': 84.00,
        'rating': 3.9,
        'reviews_count': 72,
        'image': "images/dinner/cheesy-chicken.jpg"
    },
]

for dish_data in dishes:
    if not Dish.objects.filter(name=dish_data['name']).exists():
        Dish.objects.create(**dish_data)

print('Dishes added successfully.')
