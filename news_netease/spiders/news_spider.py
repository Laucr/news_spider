# -*- coding: utf-8 -*-
# __author__ = 'Lau'

import scrapy
import sys
from news_netease.items import NewsNeteaseItem
from __init__ import xpaths_p, xpaths_tl, parse_parent_xpaths

sys.path.append('..')

reload(sys)
sys.setdefaultencoding('utf8')


class NewsNetEaseSpider(scrapy.spiders.Spider):
    def __init__(self, name=None, **kwargs):
        super(NewsNetEaseSpider, self).__init__(name, **kwargs)

    name = "netease"
    allowed_domains = ["163.com"]
    start_urls = [
        "http://news.163.com"
    ]

    # OVERRIDE
    def parse(self, response):
        # DEBUG
        self.log("--- A response from %s just arrived." % response.url)

        items = []

        obs = parse_parent_xpaths(response, xpaths_p, xpaths_tl)

        for iter_i in range(0, len(obs)):
            news_size = len(obs[iter_i]['title'][0])
            for iter_j in range(0, news_size):
                item = NewsNeteaseItem()
                item['title'] = obs[iter_i]['title'][0][iter_j]
                item['link'] = obs[iter_i]['link'][0][iter_j]
                items.append(item)

        for _item in items:
            yield scrapy.http.Request(url=_item['link'], meta={'title': _item['title']},
                                      callback=self.parse_secondary_link)

    def parse_secondary_link(self, response):
        sel = scrapy.Selector(response)
        item = NewsNeteaseItem()
        item['title'] = response.meta['title']
        txt_temp = sel.xpath('//div[@class="post_text"]/p/text()').extract()
        txt_temp += sel.xpath('//div[@class="end-text"]/p/text()').extract()
        txt_list = txt_temp
        context = ""
        for iter_ in range(0, len(txt_list)):
            context = context + txt_list[iter_]
        item['context'] = context

        yield item
