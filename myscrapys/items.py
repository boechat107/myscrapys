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


class IptuCuritibaItem(Item):
    registration_number = Field()
    sublote = Field()
    owner = Field()
    address_street = Field()
    neighborhood = Field()

    def __setitem__(self, key, value):
        if key in self.fields:
            field = self.fields[key]
            
            if isinstance(value, str) or isinstance(value, unicode):
                value = value.strip()
            self._values[key] = value
        else:
            raise KeyError("%s does not support field: %s" %
                (self.__class__.__name__, key))
