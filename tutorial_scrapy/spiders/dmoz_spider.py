from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial_scrapy.items import DmozItem

__author__ = 'mario'

class DmozSpider(BaseSpider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split('/')[-2]
        # open(filename, 'wb').write(response.body)

        sel = HtmlXPathSelector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        # scrapy crawl dmoz -o items.json -t json
        return items
