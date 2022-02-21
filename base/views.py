from django.shortcuts import render


def homePage(request):
    '''
    Домашняя страница
    
    Пара игор, пара напитков... что-то такое

    '''
    return render(request, 'base/home.html')
