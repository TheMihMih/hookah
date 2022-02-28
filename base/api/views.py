from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import GamesModel, MenuModel, OrdersModel
from .serializers import GamesSerializer, MenuSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/freetables',
        'GET api/menu',
        'GET api/games',
    ]
    return Response(routes)


@api_view(['GET'])
def getFreeTables(request):
    '''
    Подсчет количества свободных столов
    '''

    time = datetime.now()
    tables = OrdersModel.objects.filter(
        order_date__lt=time
    ).filter(
        expired_time__gt=time
    ).count()
    free_tables = 15 - tables
    return Response(free_tables)


@api_view(['GET'])
def getMenuPositions(request):
    '''
    Отображение пунктов меню
    '''
    menu = MenuModel.objects.all()
    serializer = MenuSerializer(menu, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getGames(request):
    '''
    Отображение пунктов меню
    '''
    games = GamesModel.objects.all()
    serializer = GamesSerializer(games, many=True)
    return Response(serializer.data)
