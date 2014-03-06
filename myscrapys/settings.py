# Scrapy settings for myscrapys project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'myscrapys'

SPIDER_MODULES = ['myscrapys.spiders']
NEWSPIDER_MODULE = 'myscrapys.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0'

## My configuration
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = True

## Pipelines
ITEM_PIPELINES = {
    'myscrapys.pipelines.StringCleanerPipeline': 300
}
