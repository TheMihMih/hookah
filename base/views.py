from django.shortcuts import render


def homePage(request):
    '''
    Домашняя страница
    
    '''
    return render(request, 'base/home.html')
