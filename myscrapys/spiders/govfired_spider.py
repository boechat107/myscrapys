from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item

from myscrapys.items import GovFiredItem

class GovFiredSpider(CrawlSpider):
    name = "govFired"
    start_urls = ["http://www.portaldatransparencia.gov.br/expulsoes/entrada"]
    rules = [
            ## Scrapes the links of each fired employee, guiding the spider to the
            ## employee's page description (fired reasons).
            Rule(SgmlLinkExtractor(allow=['/expulsoes/detalheServidor.*']),
                callback='parse_details')
            ]

    def parse_details(self, response):
        sel = Selector(response)
        item = GovFiredItem()

        ## Basic information.
        basictab = sel.xpath("//div[@id='resumo']/table/tbody/tr/td[2]/text()").extract()
        item['name'] = basictab[0]
        item['cpf'] = basictab[1]
        
        ## Getting all elements of the table "Destituicao"
        desctab = sel.xpath("//table[@summary='Detalhes do Servidor']/tbody/tr/td[position()=1 or position()=2]")
        ## FIXME: create a date object
        item['date'] = desctab[1].xpath("a/text()").re(r'\d+/\d+/\d+')[0]
        item['publication'] = desctab[1].xpath("a/@href").extract()[0]
        item['punishment'] = desctab[3].xpath("text()").extract()[0]
        item['occupation'] = desctab[4:6].xpath("text()").extract()
        [item['department'], item['uf']] = desctab[6:8].xpath("text()").extract()
        item['reason'] = desctab[8].xpath("text()").extract()


