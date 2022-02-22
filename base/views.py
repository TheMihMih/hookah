from datetime import datetime, timedelta
from time import strptime
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import OrdersForm
from .models import OrdersModel


def homePage(request):
    '''
    Домашняя страница
    
    Пара игор, пара напитков... что-то такое

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
        order_duration = strptime(request.POST.get('order_duration'), '%H:%M')
        date = request.POST.get('order_date_0') + ' ' + request.POST.get('order_date_1')
        
        orde_time = datetime.strptime(date, '%Y-%m-%d %H:%M')
        

        expire_time = orde_time + timedelta(
            hours=order_duration.tm_hour,
            minutes=order_duration.tm_min
        )
        
        try:
            order_exist = OrdersModel.objects.filter(
                table=request.POST.get('table')
            ).filter(
                expired_time__gt =  orde_time
            ).filter(
                order_date__lt = expire_time
            )
            if order_exist:
                messages.error(request, 'К сожалению, на данное время выбранный столик недоступен')
                print(f'К сожалению, выбранный столик в данное время не доступен')
                return redirect('make_order')
            else:
                raise ValueError
        except:
            OrdersModel.objects.create(
                user = request.user,
                table = request.POST.get('table'),
                order_date = orde_time,
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
    orders = OrdersModel.objects.all()

    context = {
        'orders': orders
    }
    return render(request, 'base/orders.html', context)
