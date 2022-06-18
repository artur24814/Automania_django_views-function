from django.shortcuts import render, redirect,get_object_or_404
import random
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from automania.forms import CarForm, OrderForm, OpinionForm
from automania.models import Car, Order, Opinion, Messeges


def homepage(request):
    all_car = Car.objects.all()
    choise = []
    for item in all_car:
        choise.append(item)
    result = {
        'car': random.choice(choise)
    }
    return render(request, "automania/homepage.html", result)

def search_views(request):
    if request.method == "POST":
        question = request.POST.get('search')
        cars = Car.objects.filter(brand__contains= question) | Car.objects.filter(type__contains = question)
        context = {
            'cars': cars,
        }
        return render(request, 'automania/search.html', context)

@login_required
def createCar(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES or None)

        if form.is_valid():
            animal = form.save(commit=False)
            animal.published = request.user
            animal.save()
            return redirect('/')
    else:
        form = CarForm()
    result = {
        'form': form
    }
    return render(request, 'automania/createCar.html', result)


def carView(request, id):
    car = Car.objects.get(id=id)
    context = {
        'car': car
    }
    return render(request, 'automania/car.html', context)

def all_car(request):
    queryset = Car.objects.all()
    result = {
        'cars': queryset
    }
    return render(request, 'automania/all_car.html', result)

@login_required
def make_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        if form.is_valid:
            animal = form.save(commit=False)
            animal.published = request.user
            animal.save()
            return redirect('/')
    else:
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request,'automania/make_order.html', context)
@login_required
def your_order(request):
    obj = Order.objects.filter(published=request.user)
    context = {
        'orders': obj
    }
    return render(request, 'automania/your_order.html', context)
@login_required
def your_posts(request):
    obj = Car.objects.filter(published=request.user)
    context = {
        'cars': obj
    }
    return render(request, 'automania/your_posts.html', context)

@login_required
def update_car(request,id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid:
            form.save()
            return redirect('/your-posts/')
    else:
        form = CarForm(instance=car)
    context = {
        'form': form,
    }
    return render(request,'automania/update-car.html', context)

@login_required
def update_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/your-order/')
    else:
        form = OrderForm(instance=order)
    context = {
        'form': form,
    }
    return render(request,'automania/update-order.html', context)

def all_opinions(request):
    queryset = Opinion.objects.all()
    context = {
        'items': queryset
    }
    return render(request, 'automania/opinions.html', context)

@login_required
def leaving_opinion(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/')
    form = OpinionForm()
    context = {
        'form': form
    }
    return render(request, 'automania/leaving_opinion.html', context)

@login_required
def messege(request, id_user):
    to_user = User.objects.get(id=id_user)
    if request.method == 'POST':

        text = request.POST.get('text')
        messege = Messeges.objects.create(from_user=request.user, to_user=to_user, text=text)
        messege.save()
        return redirect('../..')
    context = {
        'from_user': request.user,
        'to_user': to_user
    }
    return render(request, 'automania/messeges.html', context)

@login_required
def user_messeges(request):
    user_send_messeges = Messeges.objects.filter(from_user=request.user).order_by('data')
    user_got_messeges = Messeges.objects.filter(to_user= request.user).order_by('data')
    context = {
        'sends_messeges': user_send_messeges,
        'got_messeges': user_got_messeges,
    }
    return render(request, 'automania/user_meseges.html', context)



