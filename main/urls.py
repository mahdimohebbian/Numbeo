from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^country/$', views.CountryAPIView.as_view()),
    url(r'^city/$', views.CityAPIView.as_view()),

    url(r'^city/cost/$', views.CostDataAPIView.as_view()),
    url(r'^city/rent/$', views.RentDataAPIView.as_view()),
    url(r'^city/crime/$', views.CrimeDataAPIView.as_view()),
    url(r'^city/health-care/$', views.HealthCareDataAPIView.as_view()),
    url(r'^city/pollution/$', views.PollutionDataAPIView.as_view()),
    url(r'^city/traffic/$', views.TrafficDataAPIView.as_view()),
    

    url(r'^country/average/cost/$', views.AverageCostAPIView.as_view()),

    url(r'^search/$', views.SearchCityAPIView.as_view()),

]
