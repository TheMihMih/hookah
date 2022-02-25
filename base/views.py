from datetime import datetime, timedelta
from time import strptime
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate

from .forms import GamesForm, OrdersForm, MyUserCreationForm
from .models import GamesModel, OrdersModel, UserModel


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


#Бронирование столиков


def MakeOrderPage(request):
    '''
    Страница для бронирования столика

    '''
    form = OrdersForm()

    if request.method == 'POST':
        reservation_duration = strptime(request.POST.get('reservation_duration'), '%H:%M')
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


def deletePage(request, id):
    '''
    Отмена брони
    
    '''
    reservation = OrdersModel.objects.get(id=id)
    title = 'reservation'
    if request.method == 'POST':
        reservation.delete()
        return redirect('home')
    context = {
        'title': title
    }
    return render(request, 'base/delete.html', context)


#Регистрация и логин


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
    '''
    Выход из учетной записи
    '''
    logout(request)
    return redirect('home')


def loginPage(request):
    '''
    Страница входа в учетную запись
    
    '''
    page = 'login'

    context = { 'page': page }
    return render(request, 'base/login.html', context)


def processLogin(request):
    '''
    Вход в учетную запись
    
    '''
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


#Игры


def gamesPage(request):
    '''
    Страница со всеми играми
    
    '''

    games = GamesModel.objects.all()
    context = {
        'games': games
    }
    return render(request, 'base/games.html', context)


def singleGamePage(request, id):
    '''
    Подробности об определенной игре
    '''
    game = GamesModel.objects.get(id=id)
    context = {
        'game': game
    }
    return render(request, 'base/game.html', context)


def addingGamePage(request):
    '''
    Страница добавления игр
    
    '''

    form = GamesForm()
    context = {
        'form': form
    }
    return render(request, 'base/add_game.html', context)


def addingGameProcess(request):
    '''
    Добавление игры
    
    '''
    form = GamesForm()
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            try:
                exist_game = GamesModel.objects.get(
                    game_name=request.POST.get('game_name')
                )
                if exist_game:
                    print('Такая игра уже есть')
                    messages.error(request, 'Такая игра уже есть')
                    return redirect('add_game')
                else:
                    raise ValueError
            except:
                game.save()
                return redirect('home')
        else:
            messages.error(request, 'Случилась ошибка!')
            return redirect('add_game')


def deleteGame(request, id):
    '''
    Удалить игру из бд
    
    '''
    title = 'game'
    game = GamesModel.objects.get(id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('games')
    context = {
        'title': title
    }
    return render(request, 'base/delete.html', context)
