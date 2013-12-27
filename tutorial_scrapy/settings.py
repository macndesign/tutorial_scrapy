# Scrapy settings for tutorial_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial_scrapy'

SPIDER_MODULES = ['tutorial_scrapy.spiders']
NEWSPIDER_MODULE = 'tutorial_scrapy.spiders'

ITEM_PIPELINES = [
    'tutorial_scrapy.pipelines.FilterWordsPipeline',
    'tutorial_scrapy.pipelines.JsonWriterPipeline',
    'tutorial_scrapy.pipelines.XmlExportPipeline',
    'tutorial_scrapy.pipelines.JSONExportPipeline'
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial_scrapy (+http://www.yourdomain.com)'
