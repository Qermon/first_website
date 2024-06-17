import logging

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, \
    HttpResponsePermanentRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from django.views.generic import ListView

from .models import Review, Reservation, Dish, Favorites
from .forms import ReviewForm, ReservationForm





def index(request):
    data = {
        'category_selected': 'home'
    }
    dishes = Dish.objects.all()
    return render(request, 'women/index.html', {'dishes': dishes})

def about(request):
    data = {
        'category_selected': 'about'
    }
    return render(request, 'women/about.html', context=data)

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'women/menu.html', {'dishes': dishes})

def news(request):
    data = {
        'category_selected': 'news'
    }
    return render(request, 'women/news.html', context=data)


logger = logging.getLogger(__name__)

class Search(ListView):
    template_name = 'women/menu.html'
    context_object_name = 'dishes'git init

    def get_queryset(self):
        query = self.request.GET.get('q')
        logger.info(f"Search query: {query}")
        if query:
            return Dish.objects.filter(name__iregex=query)
        else:
            return Dish.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

def reviews(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('unauthorized_page')

        if 'delete' in request.POST:
            review_id = request.POST.get('review_id')
            review = get_object_or_404(Review, id=review_id)
            if review.author == request.user:
                review.delete()
                return redirect('reviews')
            else:
                return HttpResponseForbidden("You are not allowed to delete this review.")
        else:
            form = ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.save()
                return redirect('success_page')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()

    return render(request, 'women/reviews.html', {'form': form, 'reviews': reviews})


def reservations(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('authorized_page')
        if 'delete' in request.POST:
            reservation_id = request.POST.get('reservation_id')
            print(f"Trying to delete reservation with ID: {reservation_id}")
            reservation = get_object_or_404(Reservation, id=reservation_id)
            if reservation.user == request.user:
                reservation.delete()
                print("Reservation deleted successfully")
                return redirect('reservation')
            else:
                print("User does not have permission to delete this reservation")
        else:
            print("Delete action not found in POST data")
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('success_page_reservation')
    else:
        form = ReservationForm()

    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'women/reservation.html', {'form': form, 'reservations': reservations})

@login_required
def favorites(request):
    context = {'favorites': Favorites.objects.filter(user=request.user)}
    return render(request, 'women/favorites.html', context)

@login_required
def favorites_add(request, dish_id):

    dish = Dish.objects.get(id=dish_id)
    favorites = Favorites.objects.filter(user=request.user, dish=dish)

    if not favorites.exists():
        Favorites.objects.create(user=request.user, dish=dish, price=dish.price)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        favorite = favorites.first()
        favorite.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def favorites_delete(request, id):
    favorite = Favorites.objects.get(id=id)
    favorite.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def non_reserv(request):
    return render(request, 'women/non_reserv.html')
def unauthorized_page(request):
    return render(request, 'women/unauthorized_page.html')
def success_page_reservation(request):
    return render(request, 'women/success_page_reservation.html')
def success_page(request):
    return render(request, 'women/success_page.html')

def morningfresh(request):
    return render(request, 'women/morningfresh.html')

def tooplatesoup(request):
    return render(request, 'women/tooplatesoup.html')
def newsdetail(request):
    return render(request, 'women/news-detail.html')
def cheesy_chicken(request):
    return render(request, 'women/cheesy_chicken.html')
def hot_pizza(request):
    return render(request, 'women/hot_pizza.html')
def fried_chicken(request):
    return render(request, 'women/fried_chicken.html')
def spaghetti(request):
    return render(request, 'women/spaghetti.html')
def dumplings(request):
    return render(request, 'women/dumplings.html')
def kebab(request):
    return render(request, 'women/kebab.html')
def broccoli_pasta(request):
    return render(request, 'women/broccoli_pasta.html')
def meat_pie(request):
    return render(request, 'women/meat_pie.html')


def premiumsteak(request):
    return render(request, 'women/premiumsteak.html')

def safoodset(request):
    return render(request, 'women/safoodset.html')

def burgerset(request):
    return render(request, 'women/burgerset.html')

def healthysoup(request):
    return render(request, 'women/healthysoup.html')

def bakedcreamy(request):
    return render(request, 'women/bakedcreamy.html')

def salmonset(request):
    return render(request, 'women/salmonset.html')

def supersteakset(request):
    return render(request, 'women/supersteakset.html')

def breadsteakset(request):
    return render(request, 'women/breadsteakset.html')






def login(request):
    return HttpResponse("Авторизация")





def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
