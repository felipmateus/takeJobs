# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TakejobsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    description = Field()
    local = Field()
    date = Field()
    site = Field()
    link = Field()
