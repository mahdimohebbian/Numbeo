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
    def __str__(self):
        return " {} ".format(self.name)


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
    def __str__(self):
        return " {} : {} ".format(self.country.name,self.name)


class Advertisment(models.Model):
    img = models.ImageField()
    describe = models.TextField(default=" your advertisment here !")
    link = models.TextField(default="www.google.com")
    def __str__(self):
        return self.img.__str__() + " - " + self.describe