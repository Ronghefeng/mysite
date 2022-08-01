import scrapy
from scrapy_djangoitem import DjangoItem

from . import models


class HouseItem(DjangoItem):

    django_model = models.House

    json_string = scrapy.Field()


class HostItem(DjangoItem):

    django_model = models.Host


class LabelsItem(DjangoItem):

    django_model = models.Labels


class FacilityItem(DjangoItem):

    django_model = models.Facility


class CityItem(DjangoItem):

    django_model = models.City


class urlItem(scrapy.Item):

    url = scrapy.Field()
