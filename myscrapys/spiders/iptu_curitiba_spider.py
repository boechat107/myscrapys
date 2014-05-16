from scrapy.spider import Spider
from scrapy.selector import Selector
from myscrapys.items import IptuCuritibaItem


class IptuCuritibaSpider(Spider):
    name = "iptuCuritiba"

    def __init__(self, start=0, end=100, *args, **kwargs):
        super(IptuCuritibaSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.generate_urls(int(start), int(end))

    def generate_urls(self, start, end):
        """Generate a list of URLs to be scraped.
        This function is intended to be modified frequently, mainly the
        template number. Its only flexibility is the given range of values to
        be inserted into the template.
        """
        assert end > start 
        rangeNdigits = 4
        ## Registration number template without DV and sublote.
        strnum_template = "6630057%s00" # 4 digits
        assert end < 10**rangeNdigits, "Improper range"
        url_base = "http://www2.curitiba.pr.gov.br/gtm/iptu/carnet/frmRel.Carnet.aspx?txtInscrImob=%s&txtInscrSublote=%s"
        for i in range(start, end):
            ## Only even numbers are gonna be analysed.
            if i % 2 != 0:
                continue
            rangeNum = str(i).zfill(rangeNdigits)
            main = strnum_template % rangeNum
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
            ## Control information.
            fiscal = sel.xpath('//div[@class="tam10neg"]/text()').extract()
            item['registration_number'] = fiscal[0]
            item['sublote'] = fiscal[1]
            item['nature'] = fiscal[4]
            ## Owner and address information.
            info = sel.xpath('//td[@class="tam10neg"]/text()').extract()
            item['owner'] = info[0]
            item['address_street'] = info[1]
            item['neighborhood'] = info[2]
        return item
