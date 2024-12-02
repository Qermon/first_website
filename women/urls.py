from django.contrib.auth.views import LogoutView
from django.urls import path, re_path, register_converter
from . import views, admin
from . import converters
from django.conf import settings
from django.conf.urls.static import static

from .views import Search

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

    path('login/', views.login, name='login'),
    path('search/', Search.as_view(), name='search'),


    path('reviews/', views.reviews, name='reviews'),
    path('reservation/', views.reservations, name='reservation'),
    path('menu/', views.menu, name='menu'),
    path('news/', views.news, name='news'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites-add/<int:dish_id>/', views.favorites_add, name='favorites_add'),
    path('favorites-delete/<int:id>/', views.favorites_delete, name='favorites_delete'),
    path('fried-chicken/', views.fried_chicken, name='fried-chicken'),
    path('hot-pizza/', views.hot_pizza, name='hot-pizza'),
    path('spaghetti/', views.spaghetti, name='spaghetti'),
    path('dumplings/', views.dumplings, name='dumplings'),
    path('kebab/', views.kebab, name='kebab'),
    path('broccoli-pasta/', views.broccoli_pasta, name='broccoli-pasta'),
    path('meat-pie/', views.meat_pie, name='meat-pie'),
    path('cheesy-chicken/', views.cheesy_chicken, name='cheesy-chicken'),

    path('morning-fresh/', views.morningfresh, name ='morningfresh'),
    path('news-detail/', views.newsdetail, name = 'news_detail'),
    path('tooplate-soup/', views.tooplatesoup, name = 'tooplatesoup'),
    path('premium-steak/', views.premiumsteak, name ='premiumsteak'),
    path('seafood-set/', views.safoodset, name = 'safoodset'),
    path('burger-set/', views.burgerset, name = 'burgerset'),
    path('healthy-soup/', views.healthysoup, name = 'healthysoup'),
    path('baked-creamy/', views.bakedcreamy, name = 'bakedcreamy'),
    path('salmon-set/', views.salmonset, name = 'salmonset'),
    path('steak-set/', views.supersteakset, name = 'supersteakset'),
    path('bread-steak-set/', views.breadsteakset, name = 'breadsteakset'),
    path('success_page/', views.success_page, name = 'success_page'),
    path('success_page_reservation/', views.success_page_reservation, name = 'success_page_reservation'),
    path('unauthorized_page/', views.unauthorized_page, name = 'unauthorized_page'),
    path('non_reserv/', views.non_reserv, name ='non_reserv'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
