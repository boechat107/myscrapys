# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class GovFiredItem(Item):
    name = Field()
    cpf = Field()
    publication = Field()
    date = Field()
    occupation = Field()
    department = Field()
    punishment = Field()
    uf = Field()
    reason = Field()
