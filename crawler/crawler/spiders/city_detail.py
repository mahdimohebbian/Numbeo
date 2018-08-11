# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

from time import sleep
from random import randint

from main.models import City


class CostSpider(scrapy.Spider):
    name = 'cost'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/cost-of-living/country_result.jsp']

    def parse(self, response):

        city_list = City.objects.all()
        for city in city_list:
            numbeo_city_id = city.numbeo_city_id
            form_data = {
                "city_id": str(numbeo_city_id)
            }

            sleep(randint(4, 9))
            yield FormRequest.from_response(response=response,
                                            formdata=form_data,
                                            callback=self.parse_city,
                                            meta={"city_id": city.id},
                                            dont_filter=True)

    def parse_city(self, response):
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

        city = City.objects.get(id=response.meta["city_id"])
        city.cost = result_dict
        city.save()


class RentSpider(scrapy.Spider):
    name = 'rent'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/property-investment/in/']

    def parse(self, response):

        city_list = City.objects.all()
        for city in city_list:
            numbeo_city_id = city.numbeo_city_id
            form_data = {
                "city_id": str(numbeo_city_id)
            }

            sleep(randint(4, 9))
            yield FormRequest.from_response(response=response,
                                            formdata=form_data,
                                            callback=self.parse_city,
                                            meta={"city_id": city.id})

    def parse_city(self, response):
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

        city = City.objects.get(id=response.meta["city_id"])
        city.rent = result_dict
        city.save()


class CrimeSpider(scrapy.Spider):
    name = 'crime'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/crime/in/']

    def parse(self, response):

        city_list = City.objects.all()
        for city in city_list:
            numbeo_city_id = city.numbeo_city_id
            form_data = {
                "city_id": str(numbeo_city_id)
            }

            sleep(randint(4, 9))
            yield FormRequest.from_response(response=response,
                                            formdata=form_data,
                                            callback=self.parse_city,
                                            meta={"city_id": city.id})

    def parse_city(self, response):
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

        city = City.objects.get(id=response.meta["city_id"])
        city.crime = result_dict
        city.save()


class HealthCareSpider(scrapy.Spider):
    name = 'health_care'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/health-care/in/']

    def parse(self, response):

        city_list = City.objects.all()
        for city in city_list:
            numbeo_city_id = city.numbeo_city_id
            form_data = {
                "city_id": str(numbeo_city_id)
            }

            sleep(randint(4, 9))
            yield FormRequest.from_response(response=response,
                                            formdata=form_data,
                                            callback=self.parse_city,
                                            meta={"city_id": city.id})

    def parse_city(self, response):
        results = response.xpath('//*[@class="table_builder_with_value_explanation data_wide_table"]//tr')
        if results:
            result_dict = dict()

            for i in range(1, len(results)):
                title = results[i].xpath('./td[1]/text()').extract_first()
                number = results[i].xpath('./td[3]/text()').extract_first()
                result_dict[title] = number

        else:
            result_dict = "-"

        city = City.objects.get(id=response.meta["city_id"])
        city.health_care = result_dict
        city.save()


class PollutionSpider(scrapy.Spider):
    name = 'pollution'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/pollution/in/']

    def parse(self, response):

        city_list = City.objects.all()
        for city in city_list:
            numbeo_city_id = city.numbeo_city_id
            form_data = {
                "city_id": str(numbeo_city_id)
            }

            sleep(randint(4, 9))
            yield FormRequest.from_response(response=response,
                                            formdata=form_data,
                                            callback=self.parse_city,
                                            meta={"city_id": city.id})

    def parse_city(self, response):
        results = response.xpath('//*[@class="table_builder_with_value_explanation data_wide_table"][1]//tr')
        if results:
            result_dict = dict()

            for row in results:
                title = row.xpath('./td[1]/text()').extract_first()
                value = row.xpath('./td[3]/text()').extract_first()
                result_dict[title] = value

        else:
            result_dict = "-"

        city = City.objects.get(id=response.meta["city_id"])
        city.pollution = result_dict
        city.save()


class TrafficSpider(scrapy.Spider):
    name = 'traffic'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/traffic/in/']

    def parse(self, response):

        city_list = City.objects.all()
        for city in city_list:
            numbeo_city_id = city.numbeo_city_id
            form_data = {
                "city_id": str(numbeo_city_id)
            }

            sleep(randint(4, 9))
            yield FormRequest.from_response(response=response,
                                            formdata=form_data,
                                            callback=self.parse_city,
                                            meta={"city_id": city.id})

    def parse_city(self, response):
        head_titles = response.xpath("//h3/text()").extract()
        if head_titles:
            tables = response.xpath('//h3[text()="Main Means of Transportation to Work or School"]//following-sibling::table')
            result_dict = dict()
            for i in range(0, len(head_titles)):
                table = tables[i]
                table_dict = dict()
                rows = table.xpath(".//tr")
                for row in rows:
                    title = row.xpath('./td[1]/text()').extract_first()
                    if title == None :
                        title = "Overall"
                    try:
                        value = row.xpath('./td[2]//*[@class="barTextRight"]/text()').extract_first().split('\n')[1]
                    except:
                        value = row.xpath('./td[2]//*[@class="barTextRight"]/text()').extract_first()
                    table_dict[title] = value

                result_dict[head_titles[i]] = table_dict

        else:
            result_dict = "-"

        city = City.objects.get(id=response.meta["city_id"])
        city.traffic = result_dict
        city.save()
