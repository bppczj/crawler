# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from lxml import etree
from spyderA.items import SpyderaItem

class CuiqingcaiSpider(scrapy.Spider):
    name = 'cuiqingcai'
    allowed_domains = ['cuiqingcai.com']
    start_url = 'https://cuiqingcai.com/'
    # start_urls = ['https://cuiqingcai.com/']

    def parse(self, response):
        tree = etree.HTML(response.text)
        item = SpyderaItem()
        for article in tree.xpath('//div/article'):
            print article.xpath('.//h2/a[@title]')[0].text
            item['title']=article.xpath('.//h2/a[@title]')[0].text
            print article.xpath('.//span//a')[0].text
            item['author']=article.xpath('.//span//a')[0].text
            yield item

    def start_requests(self):
        url = self.start_url
        yield Request(url, self.parse)

