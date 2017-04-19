import re
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
#from scrapy.selector import Selector
#from scrapy.http import Request
from ..items import DoubangroupItem

import sys
reload(sys)
default_encoding = 'utf-8'
sys.setdefaultencoding(default_encoding)

class DoubangroupSpider(CrawlSpider):
    name = 'DoubanGroupSpider'
    allowed_domains = ['www.douban.com']
    start_urls = [
            'https://www.douban.com/group/explore?&tag=%E8%B4%AD%E7%89%A9',
            'https://www.douban.com/group/explore?tag=%E5%85%B4%E8%B6%A3',
            'https://www.douban.com/group/explore?tag=%E7%94%9F%E6%B4%BB',
            'https://www.douban.com/group/explore?tag=%E7%A4%BE%E4%BC%9A',
            'https://www.douban.com/group/explore?tag=%E8%89%BA%E6%9C%AF',
            'https://www.douban.com/group/explore?tag=%E5%AD%A6%E6%9C%AF',
            'https://www.douban.com/group/explore?tag=%E6%83%85%E6%84%9F',
            'https://www.douban.com/group/explore?tag=%E9%97%B2%E8%81%8A'
    ]

    rules = [
        Rule(LinkExtractor(allow=(r'start=[0-9]',r'start=[1-9][0-9]', r'start=[1-9][0-9][0-9]', r'start=[1-9][0-9][0-9][0-9]')),
        callback='parse_cookie', follow=True,process_request='add_cookie')
    ]

    def add_cookie(self, request):
		request.replace(cookies=[
            {



                },
            ]);
		return request;

    def parse_cookie(self, response):
        group_list = response.css('div.group-list div.result')
        items = []
        for group in group_list:
            item = DoubangroupItem()
            try:
                item['title'] = group.xpath('div[2]/div[1]/h3/a/text()').extract()[0]
                item['group_url'] = group.xpath('div[2]/div[1]/h3/a/@href').extract()[0]
                item['members'] = group.xpath('div[2]/div[2]/text()').extract()[0]
                item['content'] = group.xpath('div[2]/p/text()').extract()[0]
            except:
                pass
            items.append(item)
        return items
