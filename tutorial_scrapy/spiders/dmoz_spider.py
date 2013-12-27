from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial_scrapy.items import DmozItem
import subprocess


class DmozSpider(BaseSpider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "http://www.dmoz.org/Computers/Programming/Languages/JavaScript/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/JavaScript/Scripts/"
    ]

    def parse(self, response):
        # Getting HTML content
        # lang = response.url.split('/')[-3].lower()
        # content = response.url.split('/')[-2].lower()
        # filename = '{0}-{1}.html'.format(lang, content)
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
