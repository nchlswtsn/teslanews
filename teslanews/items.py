# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class TeslanewsItem(Item):
    date = Field()
    title = Field()
    url = Field()


