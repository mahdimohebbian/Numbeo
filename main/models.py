from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    currency_code = models.CharField(max_length=5, null=True)
    currency_sign = models.CharField(max_length=10, null=True)
    exchange_rate = models.CharField(max_length=10, null=True)
    created = models.DateField(auto_now_add=True)

    avg_cost = models.TextField()
    avg_rent = models.TextField()
    avg_crime = models.TextField()
    avg_health_care = models.TextField()
    avg_pollution = models.TextField()
    avg_traffic = models.TextField()


class City(models.Model):
    country = models.ForeignKey(Country, null=True)
    numbeo_city_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    cost = models.TextField()
    rent = models.TextField()
    crime = models.TextField()
    health_care = models.TextField()
    pollution = models.TextField()
    traffic = models.TextField()
