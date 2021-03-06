from django.shortcuts import render, redirect,get_object_or_404
import random
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .forms import CarForm, OrderForm, OpinionForm
from .models import Car, Order, Opinion, Messeges, ReadedMesseges


def homepage(request):
    """
    views for homepage
    """
    all_car = Car.objects.all()
    #if we have empty list of all car
    if len(all_car) == 0:
        return render(request, "automania/homepage.html", {})
    #if not empty we choose random car to show in a homepage
    choise = []
    for item in all_car:
        choise.append(item)
    result = {
        'car': random.choice(choise)
    }
    return render(request, "automania/homepage.html", result)

def search_views(request):
    """
    view for search accordingly filtering by fields 'brand' and 'type'
    """
    if request.method == "POST":
        question = request.POST.get('search')
        cars = Car.objects.filter(brand__contains= question) | Car.objects.filter(type__contains = question)
        context = {
            'cars': cars,
        }
        return render(request, 'automania/search.html', context)

@login_required
def create_car(request):
    """
    views for creating new car, not log in users will be redirect to /login/
    """
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES or None)

        if form.is_valid():
            new_car = form.save(commit=False)
            new_car.published = request.user
            new_car.save()
            return redirect('/')
        else:
            return render(request, 'automania/createCar.html', {'form': form})
    else:
        form = CarForm()
    result = {
        'form': form
    }
    return render(request, 'automania/createCar.html', result)


def car_detail(request, id):
    """
    views car detail
    """
    car = get_object_or_404(Car, id=id)
    context = {
        'car': car
    }
    return render(request, 'automania/car.html', context)

def all_car(request):
    """
    views list all car
    """
    queryset = Car.objects.all()
    result = {
        'cars': queryset
    }
    return render(request, 'automania/all_car.html', result)

@login_required
def make_order(request):
    """
    views for make order, not log in users will be redirect to /login/
    """
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
    """
    view for user own orders
    """
    obj = Order.objects.filter(published=request.user)
    context = {
        'orders': obj
    }
    return render(request, 'automania/your_order.html', context)


@login_required
def your_posts(request):
    """
    view for user own posts
    """
    obj = Car.objects.filter(published=request.user)
    context = {
        'cars': obj
    }
    return render(request, 'automania/your_posts.html', context)

@login_required
def update_car(request,id):
    """
    view for update car
    """
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
    """
    view for update order
    """
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
    """
    views for make opinion
    """
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
    """
    view for create message to user with id_user,
    plus create unread message and inform user about that with using context_processor
    """
    to_user = get_object_or_404(User, id=id_user)
    if request.method == 'POST':

        text = request.POST.get('text')
        #create message
        message = Messeges.objects.create(from_user=request.user, to_user=to_user, text=text)
        #create unread message
        unread_message = ReadedMesseges.objects.create(owner=to_user.username, message=message)
        message.save()
        return redirect('/user-messeges/')
    context = {
        'from_user': request.user,
        'to_user': to_user
    }
    return render(request, 'automania/messeges.html', context)

@login_required
def user_messeges(request):
    """
    views for user own messages,
    unread messages collected for shown it in another color
    """
    all_unread_or_read_message = ReadedMesseges.objects.filter(owner=request.user.username).order_by('data')
    user_send_messeges = Messeges.objects.filter(from_user=request.user).order_by('data')
    user_got_messeges = Messeges.objects.filter(to_user= request.user).order_by('data')
    context = {
        'all_unread_or_read_message': all_unread_or_read_message,
        'sends_messeges': user_send_messeges,
        'got_messeges': user_got_messeges,
    }
    return render(request, 'automania/user_meseges.html', context)

@login_required
def answer_to_messege(request, id_user, id_message):
    """
    views for make answer for message and make this message read put read to "True"
    """
    read_message = get_object_or_404(ReadedMesseges,id=id_message)
    read_message.read = True
    read_message.save()
    to_user = get_object_or_404(User, id=id_user)
    if request.method == 'POST':

        text = request.POST.get('text')
        #create message
        message = Messeges.objects.create(from_user=request.user, to_user=to_user, text=text)
        #create unread message
        unread_message = ReadedMesseges.objects.create(owner=to_user.username, message=message)
        message.save()
        redirect('/user-messeges/')
    context = {
        'from_user': request.user,
        'to_user': to_user
    }
    return render(request, 'automania/messeges.html', context)

@login_required
def delete_message(request, id_message):
    """
    view for delete message
    """
    delete_messege = get_object_or_404(Messeges, id=id_message)
    delete_messege.delete()
    return redirect('/user-messeges')



