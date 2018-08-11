# -*- coding: utf-8 -*-
import json

import scrapy

from time import sleep
from random import randint
from main.models import Country
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class AvgCostSpider(scrapy.Spider):
    name = 'avg_cost'

    def start_requests(self):

        country_list = Country.objects.all()
        for country in country_list:
            sleep(randint(4, 9))
            url = "https://www.numbeo.com/cost-of-living/country_result.jsp?country={}".format(country.name)
            yield scrapy.Request(url=url, callback=self.parse_country, meta={"country_id": country.id})

    def parse_country(self, response):
        results = response.xpath('//table[@class="data_wide_table"]//tr')
        if results:
            result_dict = dict()
            last_category = ""
            data = dict()
            for i in range(0, len(results)):

                if len(results[i].xpath('.//*[@class="highlighted_th prices"]')) != 0:
                    if last_category != "":
                        result_dict[last_category] = data
                        data = dict()

                    last_category = results[i].xpath('.//*[@class="highlighted_th prices"]/text()').extract()[0]
                else:
                    # ---- numbers ----
                    numbers = results[i].xpath('.//td[2]/text()').extract()[0]
                    final_str = numbers.split(' ')[1]
                    final_str = final_str.replace("\u00a0", "")
                    final_str = final_str.replace("\u20ac", "")

                    # ==== title of the number ====
                    title = results[i].xpath('.//td[1]/text()').extract()[0]

                    data[title] = final_str

                    if i == len(results) - 1:
                        result_dict[last_category] = data

        else:
            result_dict = "-"

        country = Country.objects.get(id=response.meta["country_id"])
        country.avg_cost = result_dict
        country.save()


class AvgRentSpider(scrapy.Spider):
    name = 'avg_rent'

    def start_requests(self):

        country_list = Country.objects.all()
        for country in country_list:
            sleep(randint(4, 9))
            url = "https://www.numbeo.com/property-investment/country_result.jsp?country={}".format(country.name)
            yield scrapy.Request(url=url, callback=self.parse_country, meta={"country_id": country.id})

    def parse_country(self, response):
        results = response.xpath('//table[@class="data_wide_table"]//tr')
        if results:
            result_dict = dict()
            last_category = ""
            data = dict()

            for i in range(0, len(results)):

                if len(results[i].xpath('.//*[@class="highlighted_th prices"]')) != 0:
                    if last_category != "":
                        result_dict[last_category] = data
                        data = dict()

                    last_category = results[i].xpath('.//*[@class="highlighted_th prices"]/text()').extract()[0]
                else:

                    # ---- number
                    numbers = results[i].xpath('.//td[2]/text()').extract()[0]
                    final_str = numbers.split(' ')[1]
                    final_str = final_str.replace("\u00a0", "")
                    final_str = final_str.replace("\u20ac", "")

                    # ==== title of the number
                    title = results[i].xpath('.//td[1]/text()').extract()[0]

                    data[title] = final_str

                    if i == len(results) - 1:
                        result_dict[last_category] = data

        else:
            result_dict = "-"

        country = Country.objects.get(id=response.meta["country_id"])
        country.avg_rent = result_dict
        country.save()


class AvgCrimeSpider(scrapy.Spider):
    name = 'avg_crime'

    def start_requests(self):

        country_list = Country.objects.all()
        for country in country_list:
            sleep(randint(4, 9))
            url = "https://www.numbeo.com/crime/country_result.jsp?country={}".format(country.name)
            yield scrapy.Request(url=url, callback=self.parse_country, meta={"country_id": country.id})

    def parse_country(self, response):
        results = response.xpath('//*[@class="table_builder_with_value_explanation data_wide_table"]')
        if results:
            result_dict = dict()
            rows = results[0].xpath('.//tr')

            for row in rows:
                title = row.xpath('./td[1]/text()').extract_first()
                score = row.xpath('./td[3]/text()').extract_first()
                result_dict[title] = score

            rows = results[1].xpath('.//tr')

            for row in rows:
                title = row.xpath('./td[1]/text()').extract_first()
                score = row.xpath('./td[3]/text()').extract_first()
                result_dict[title] = score

        else:
            result_dict = "-"

        country = Country.objects.get(id=response.meta["country_id"])
        country.avg_crime = result_dict
        country.save()


class AvgHealthCareSpider(scrapy.Spider):
    name = 'avg_health_care'

    def start_requests(self):

        country_list = Country.objects.all()
        for country in country_list:
            sleep(randint(4, 9))
            url = "https://www.numbeo.com/health-care/country_result.jsp?country={}".format(country.name)
            yield scrapy.Request(url=url, callback=self.parse_country, meta={"country_id": country.id})

    def parse_country(self, response):
        results = response.xpath('//*[@class="table_builder_with_value_explanation data_wide_table"]//tr')
        if results:
            result_dict = dict()

            for i in range(1, len(results)):
                title = results[i].xpath('./td[1]/text()').extract_first()
                number = results[i].xpath('./td[3]/text()').extract_first()
                result_dict[title] = number

        else:
            result_dict = "-"

        country = Country.objects.get(id=response.meta["country_id"])
        country.avg_health_care = result_dict
        country.save()


class AvgPollutionSpider(scrapy.Spider):
    name = 'avg_pollution'

    def start_requests(self):

        country_list = Country.objects.all()
        for country in country_list:
            sleep(randint(4, 9))
            url = "https://www.numbeo.com/pollution/country_result.jsp?country={}".format(country.name)
            yield scrapy.Request(url=url, callback=self.parse_country, meta={"country_id": country.id})

    def parse_country(self, response):
        results = response.xpath('//*[@class="table_builder_with_value_explanation data_wide_table"][1]//tr')
        if results:
            result_dict = dict()

            for row in results:
                title = row.xpath('./td[1]/text()').extract_first()
                value = row.xpath('./td[3]/text()').extract_first()
                result_dict[title] = value

        else:
            result_dict = "-"

        country = Country.objects.get(id=response.meta["country_id"])
        country.avg_pollution = result_dict
        country.save()


class AvgTrafficSpider(scrapy.Spider):
    name = 'avg_traffic'

    def start_requests(self):

        country_list = Country.objects.all()
        for country in country_list:
            sleep(randint(4, 9))
            url = "https://www.numbeo.com/traffic/country_result.jsp?country={}".format(country.name)
            yield scrapy.Request(url=url, callback=self.parse_country, meta={"country_id": country.id})

    def parse_country(self, response):
        head_titles = response.xpath("//h3/text()").extract()
        if head_titles:
            tables = response.xpath(
                '//h3[text()="Main Means of Transportation to Work or School"]//following-sibling::table')
            result_dict = dict()
            for i in range(0, len(head_titles)):
                table = tables[i]
                table_dict = dict()
                rows = table.xpath(".//tr")
                for row in rows:
                    title = row.xpath('./td[1]/text()').extract_first()
                    if title == None:
                        title = "Overall"
                    try:
                        value = row.xpath('./td[2]//*[@class="barTextRight"]/text()').extract_first().split('\n')[1]
                    except:
                        value = row.xpath('./td[2]//*[@class="barTextRight"]/text()').extract_first()
                    table_dict[title] = value

                result_dict[head_titles[i]] = table_dict

        else:
            result_dict = "-"

        country = Country.objects.get(id=response.meta["country_id"])
        country.avg_traffic = result_dict
        country.save()
