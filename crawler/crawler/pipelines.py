# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from main.models import Country, City


class CrawlerPipeline(object):
    def process_item(self, data_set, spider):
        print("\n\n------- pipline-------")

        if spider.name == "country":
            return self.handle_country(data_set)

        elif data_set["db_table"] == "Country":
            return self.handle_country(data_set)

        elif data_set["db_table"] == "City":
            return self.handle_city(data_set)

    def handle_country(self, data_set):
        print("-------handle_country-------")

        item = Country()
        item.name = data_set["name"]
        item.currency = data_set["currency"]
        item.save()

    def handle_city(self, data_set):
        print("-------handle_city-------")

        item = City()
        item.name = data_set["name"]
        country_name = data_set["country_name"]
        country = Country.objects.filter(name=country_name).last()
        item.country = country
        item.save()
