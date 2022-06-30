import scrapy

class WangyiproItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()