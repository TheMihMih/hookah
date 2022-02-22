from datetime import datetime, timedelta
from multiprocessing import context
from time import strptime
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

from .forms import OrdersForm, MyUserCreationForm
from .models import OrdersModel, UserModel


def homePage(request):
    '''
    Домашняя страница
    
    Пара игр, пара напитков... что-то такое

    '''

    list_ = [1, 2, 3 , 4]
    context = {
        'list': list_
    }
    return render(request, 'base/home.html', context)


def MakeOrderPage(request):
    '''
    Страница для бронирования столика

    '''
    form = OrdersForm()

    if request.method == 'POST':
        reservation_duration = strptime(request.POST.get('order_duration'), '%H:%M')
        date = request.POST.get('order_date_0') + ' ' + request.POST.get('order_date_1')
        reservation_time = datetime.strptime(date, '%Y-%m-%d %H:%M')
        expire_time = reservation_time + timedelta(
            hours=reservation_duration.tm_hour,
            minutes=reservation_duration.tm_min
        )
        order_exist = OrdersModel.objects.filter(
            table=request.POST.get('table')
        ).filter(
            expired_time__gt =  reservation_time
        ).filter(
            order_date__lt = expire_time
        )

        if order_exist:
            messages.error(request, 'К сожалению, на данное время выбранный столик недоступен')
            return redirect('make_order')

        OrdersModel.objects.create(
            user = request.user,
            table = request.POST.get('table'),
            order_date = reservation_time,
            expired_time = expire_time
        )
        return redirect('home')

    context = { 'form': form }
    return render(request, 'base/make_order.html', context)


def CheckOrdersPage(request):
    '''
    Страница для просмотра бронирования
    Stuff only
    '''
    time = datetime.now()
    if request.user.is_staff:
        orders = OrdersModel.objects.filter(expired_time__gt=time)
    else:
        orders = OrdersModel.objects.filter(user=request.user)

    context = {
        'orders': orders
    }
    return render(request, 'base/orders.html', context)


def registerPage(request):
    """
    Страница регистрации
    """
    form = MyUserCreationForm()
    context ={
        'form': form
    }
    return render(request, 'base/login.html', context)


def processRegistration(request):
    """
    Процесс регистрации
    """
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                user_exist = UserModel.objects.get(phone=user.phone)
                if user_exist:
                    messages.error(request, 'Ошибка! Пользователь уже существует')
                    return redirect('login')
            except:
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'Случилась ошибка!')
            return redirect('register')


def logoutPage(request):
    logout(request)
    return redirect('home')


def loginPage(request):
    page = 'login'

    context = { 'page': page }
    return render(request, 'base/login.html', context)


def processLogin(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            user = UserModel.objects.get(phone=phone)
        except:
            messages.error(request, 'Пользователь не найден!')
            return redirect('register')
        
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Произошла ошибка!')
            return redirect('login')
