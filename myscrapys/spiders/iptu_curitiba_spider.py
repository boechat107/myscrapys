from scrapy.spider import Spider
from scrapy.selector import Selector
from myscrapys.items import IptuCuritibaItem


class IptuCuritibaSpider(Spider):
    name = "iptuCuritiba"

    def __init__(self, *args, **kwargs):
        super(IptuCuritibaSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.generate_urls()

    def generate_urls(self):
        """Generate a list of URLs to be scraped.
        """
        url_base = "http://www2.curitiba.pr.gov.br/gtm/iptu/carnet/frmRel.Carnet.aspx?txtInscrImob=%s&txtInscrSublote=%s"
        main_template = "662007400%s00" # 2 digits
        ## TODO: specify the range by command line.
        for i in range(30, 34):
            main = main_template % i
            main = main + str(self.dv(main))
            sublote = '000'
            self.log("Registration number: %s|%s" % (main, sublote))
            yield url_base % (main, sublote)

    def dv(self, numStr):
        """Calculates the digit verifier.
        """
        sum = 0
        for x in range(1,13):
            sum = sum + int(numStr[13-x])*x
            return sum%13%10

    def parse(self, response):
        sel = Selector(response)
        item = IptuCuritibaItem()
        ## Checking the existence. 
        exist = sel.xpath("head/title/text()").extract()[0]
        if exist == 'Erro':
            item['registration_number'] = 'not found'
        else:
            fiscal = sel.xpath('//div[@class="tam10neg"]/text()').extract()
            item['registration_number'] = fiscal[0]
            item['sublote'] = fiscal[1]
            info = sel.xpath('//td[@class="tam10neg"]/text()').extract()
            item['owner'] = info[0]
            item['address_street'] = info[1]
            item['neighborhood'] = info[2]
        return item
