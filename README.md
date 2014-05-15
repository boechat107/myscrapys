# myscrapys

Just my personal repository of scrapers using the
[Scrapy](http://doc.scrapy.org/en/latest/intro/overview.html) framework.
For now, it comes just for learning purposes.

## List of implemented scrapers

### GovFiredSpider

Fired public employees of Brazil, 
[Portal Transparência](http://www.portaldatransparencia.gov.br/expulsoes/entrada).

* There are multiple pages to be scraped (pagination).
* Some targets, employees, have more than one dismissal table (containing
information like occupation, department, reasons...).
* Not implemented yet:
    + There is no data treatment yet (there are empty spaces of fields).
    + Only the first page is captured for now (it should be solved very soon).

### IptuCuritibaSpider

It is intended to scrape information about properties of 
[Curitiba city](http://www2.curitiba.pr.gov.br/gtm/iptu/carnet/default.aspx).

* Not all data is been scraped, more fields need to be added.
* It's very hard to generate existent register numbers.
