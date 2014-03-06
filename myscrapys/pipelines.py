# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StringCleanerPipeline(object):
    """
    Prepares string values, like removing unnecessary white spaces.
    """

    def clean(self, value):
        if isinstance(value, list):
            outlist = []
            for v in value:
                outlist.append(self.clean(v))
            return outlist
        ## The method extract() always returns an unicode string.
        elif isinstance(value, str) or isinstance(value, unicode):
            return value.strip()
        else:
            return value

    def process_item(self, item, spider):
        for k, v in item.iteritems():
            item[k] = self.clean(v)
        return item
