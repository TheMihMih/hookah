from re import M
from rest_framework.serializers import ModelSerializer
from base.models import GamesModel, MenuModel


class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'


class GamesSerializer(ModelSerializer):
    class Meta:
        model = GamesModel
        fields = '__all__'
