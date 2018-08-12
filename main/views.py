from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework import status
from rest_framework.response import Response

# this item is for converting string into actual dictionary
import ast

'''
a hint on how to convert a string dictionary to an actual dictionary :

>>> import ast
>>> ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
{'muffin': 'lolz', 'foo': 'kitty'}

'''


class CountryAPIView(APIView):
    def get(self, request):
        """APIView designed to retrieve all countries objects."""

        countries = models.Country.objects.all()
        serializer = serializers.CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CityAPIView(APIView):
    def post(self, request):
        """APIView designed to retrieve country's cities data."""

        country_serializer = serializers.CountrySelectorSerializer(data=request.data)
        if country_serializer.is_valid():
            country_id = country_serializer.validated_data["country_id"]
            try:
                country = models.Country.objects.get(id=country_id)
                cities = models.City.objects.filter(country_id=country.id)
                city_serializer = serializers.CityAbstractSerializer(cities, many=True)
                return Response(city_serializer.data, status=status.HTTP_200_OK)

            except models.Country.DoesNotExist:
                return Response({"message": "This country doesn't exist!"}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------- returning raw data from crawled data in database

def city_selector(request):
    """function for select a specific city by its id and return it."""

    city_serializer = serializers.CitySelectorSerializer(data=request.data)
    if city_serializer.is_valid():
        city_id = city_serializer.validated_data["city_id"]
        try:
            city = models.City.objects.get(id=city_id)
            return city

        except models.Country.DoesNotExist:
            return Response({"message": "This city doesn't exist!"}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CostDataAPIView(APIView):
    def post(self, request):
        """APIView designed to retrieve specific city cost data"""

        city = city_selector(request)
        if city.traffic:
            result_dict = ast.literal_eval(city.cost)
        else:
            result_dict = {}
        return Response(result_dict, status=status.HTTP_200_OK)


class RentDataAPIView(APIView):
    def post(self, request):
        """APIView designed to retrieve specific city rent data"""

        city = city_selector(request)
        if city.traffic:
            result_dict = ast.literal_eval(city.rent)
        else:
            result_dict = {}
        return Response(result_dict, status=status.HTTP_200_OK)


class CrimeDataAPIView(APIView):
    def post(self, request):
        """APIView designed to retrieve specific city crime data"""

        city = city_selector(request)
        if city.traffic:
            result_dict = ast.literal_eval(city.crime)
        else:
            result_dict = {}
        return Response(result_dict, status=status.HTTP_200_OK)


class HealthCareDataAPIView(APIView):
    def post(self, request):
        """APIView designed to retrieve specific city health care data"""

        city = city_selector(request)
        if city.traffic:
            result_dict = ast.literal_eval(city.health_care)
        else:
            result_dict = {}
        return Response(result_dict, status=status.HTTP_200_OK)


class PollutionDataAPIView(APIView):

    def post(self, request):
        """APIView designed to retrieve specific city pollution data"""

        city = city_selector(request)
        if city.traffic:
            result_dict = ast.literal_eval(city.pollution)
        else:
            result_dict = {}
        return Response(result_dict, status=status.HTTP_200_OK)


class TrafficDataAPIView(APIView):

    def post(self, request):
        """APIView designed to retrieve specific city traffic data"""

        city = city_selector(request)
        if city.traffic:
            result_dict = ast.literal_eval(city.traffic)
        else:
            result_dict = {}
        return Response(result_dict, status=status.HTTP_200_OK)


# ----------------------------------------------------


# APIs for returning all of the cities in a country for comparison :

class AllCitiesRentAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_name = request.data['country']
        country = models.Country.objects.get(name=country_name)
        cities = models.City.objects.filter(country=country)
        result_list = list()
        for city in cities:
            result_list.append({city.name.__str__(): ast.literal_eval(city.rent)})

        return Response(result_list, status=status.HTTP_200_OK)


class AllCitiesCostAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_name = request.data['country']
        country = models.Country.objects.get(name=country_name)
        cities = models.City.objects.filter(country=country)
        result_list = list()
        for city in cities:
            result_list.append({city.name.__str__(): ast.literal_eval(city.cost)})

        return Response(result_list, status=status.HTTP_200_OK)


class AllCitiesHealthCareAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_name = request.data['country']
        country = models.Country.objects.get(name=country_name)
        cities = models.City.objects.filter(country=country)
        result_list = list()
        for city in cities:
            result_list.append({city.name.__str__(): ast.literal_eval(city.health_care)})

        return Response(result_list, status=status.HTTP_200_OK)


class AllCitiesPollutionAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_name = request.data['country']
        country = models.Country.objects.get(name=country_name)
        cities = models.City.objects.filter(country=country)
        result_list = list()
        for city in cities:
            result_list.append({city.name.__str__(): ast.literal_eval(city.pollution)})

        return Response(result_list, status=status.HTTP_200_OK)


class AllCitiesTrafficAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_name = request.data['country']
        country = models.Country.objects.get(name=country_name)
        cities = models.City.objects.filter(country=country)
        result_list = list()
        for city in cities:
            result_list.append({city.name.__str__(): ast.literal_eval(city.traffic)})

        return Response(result_list, status=status.HTTP_200_OK)


class AllCitiesCrimeAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_name = request.data['country']
        country = models.Country.objects.get(name=country_name)
        cities = models.City.objects.filter(country=country)
        result_list = list()
        for city in cities:
            result_list.append({city.name.__str__(): ast.literal_eval(city.crime)})

        return Response(result_list, status=status.HTTP_200_OK)


# --------------------------------

# APIs to get the averegae of a country's cities by it's parameters, like crime 

class AverageRentAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_id = int(request.data["country_id"])
        country = models.Country.objects.get(id=country_id)
        result_data = ast.literal_eval(country.avg_rent)

        return Response(result_data,status=status.HTTP_200_OK)


class AverageCostAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_id = int(request.data["country_id"])
        country = models.Country.objects.get(id=country_id)
        result_data = ast.literal_eval(country.avg_cost)

        return Response(result_data,status=status.HTTP_200_OK)


class AverageCrimeAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_id = int(request.data["country_id"])
        country = models.Country.objects.get(id=country_id)
        result_data = ast.literal_eval(country.avg_crime)

        return Response(result_data,status=status.HTTP_200_OK)


class AverageHealthcareAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_id = int(request.data["country_id"])
        country = models.Country.objects.get(id=country_id)
        result_data = ast.literal_eval(country.avg_health_care)

        return Response(result_data,status=status.HTTP_200_OK)


class AveragePollutionAPIView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        country_id = int(request.data["country_id"])
        country = models.Country.objects.get(id=country_id)
        result_data = ast.literal_eval(country.avg_pollution)

        return Response(result_data,status=status.HTTP_200_OK)
        

class SearchCityAPIView(APIView):
    def get(self,request):
        input_data = request.query_params.get('search',None)
        cities = models.City.objects.filter(name__startswith=input_data)
        serializer = serializers.CityAbstractSerializer(cities,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,reuqest):
        pass

class AdvertismentAPIView(APIView):
    def get(self,request):
        ads = models.Advertisment.objects.all()
        serializer = serializers.AdvertiseSerializer(ads,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        pass # this api post would not be needed cause it can be done by Django Admin