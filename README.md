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
