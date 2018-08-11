# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from time import sleep
from random import randint
from main.models import Country, City
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class CountryAndCitySpider(scrapy.Spider):
    name = 'country_and_city'
    allowed_domains = ['numbeo.com']
    start_urls = ['http://numbeo.com']

    def parse(self, response):
        Country.objects.all().delete()
        City.objects.all().delete()

        country_list = response.xpath('//*[@id="country"]//option/text()').extract()[1:40]
        for country in country_list:
            sleep(randint(4, 9))

            new_country = Country(name=country)
            new_country.save()

            yield scrapy.Request(
                "https://numbeo.com/cost-of-living/country_result.jsp?country={}".format(country),
                callback=self.parse_city,
                meta={"country_id": new_country.id})

    def parse_city(self, response):
        print("\n\n---------url-------", response.url)
        price = response.xpath("//table[@class='data_wide_table']//tr[2]/td[2]/text()").extract_first()
        currency_sign = price.split("\xa0")[1]
        currency_code = response.xpath("//select[@id='displayCurrency']/option[@selected='selected']/text()").extract_first()

        country = Country.objects.get(id=response.meta["country_id"])
        country.currency_sign = currency_sign
        country.currency_code = currency_code
        country.save()

        city_list = response.xpath('//*[@id="city"]//option/text()').extract()[1:]
        for city in city_list:
            city = City(country=country, name=city)
            city.save()


class ExchangeRateSpider(scrapy.Spider):
    name = 'exchange_rate'
    allowed_domains = ['numbeo.com/common/currency_settings.jsp']
    start_urls = ['http://numbeo.com/common/currency_settings.jsp']

    def parse(self, response):
        tr_list = response.xpath("//table[@id='t2']//tr")[1:]
        for tr in tr_list:
            currency_code = tr.xpath(".//td/text()").extract()[0]
            exchange_rate = tr.xpath(".//td/text()").extract()[1]

            try:
                country_list = Country.objects.filter(currency_code=currency_code)
                for country in country_list:
                    country.exchange_rate = exchange_rate
                    country.save()

            except Country.DoesNotExist:
                print("Country object doesn't exist.")


class CityCodeSpider(scrapy.Spider):
    name = 'city_code'

    def start_requests(self):
        city_list = City.objects.all()

        for city in city_list:
            city_name = city.name
            url = "https://www.numbeo.com/common/CitySearchJson?term={},{}".format(city_name, city.country.name)
            yield scrapy.Request(url=url, callback=self.parse, meta={"city_id": city.id})

    def parse(self, response):
        numbeo_city_id = json.loads(response.body_as_unicode())[0]["value"]
        city = City.objects.get(id=response.meta["city_id"])
        city.numbeo_city_id = numbeo_city_id
        city.save()






# configure_logging()
# runner = CrawlerRunner()
#
# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(CountryAndCitySpider)
#     yield runner.crawl(ExchangeRateSpider)
#     yield runner.crawl(CityCodeSpider)
#     yield runner.crawl(AvgCostSpider)
#     reactor.stop()
#
# crawl()
# reactor.run() # the script will block here until the last crawl call is finished
