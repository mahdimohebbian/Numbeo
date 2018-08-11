from rest_framework import serializers
from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class CountrySelectorSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()


class CityAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'name')


# serializer class for Abstract Country model
class CitySelectorSerializer(serializers.Serializer):
    city_id = serializers.IntegerField()
