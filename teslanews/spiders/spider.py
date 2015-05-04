# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from teslanews.items import TeslanewsItem


class MySpider(BaseSpider):
	name = "teslanews"
	allowed_domains = ["teslamotors.com"]
	start_urls = ["http://www.teslamotors.com/blog"]

	def parse(self, response):
		updates = hxs.xpath('//div[@class="blog-wrapper no-image"]')
		base = "http://www.teslamotors.com"
		items = []
		for article in updates:
			item = TeslanewsItem()
			item["date"] =  article.xpath('./div/span/span/text()').extract()
			item["title"] = article.xpath('./h2/a/text()').extract()
			item["url"] = article.xpath('./h2/a/@href').extract()
			item["url"] = base + article.xpath('./h2/a/@href').extract()[0]
			items.append(item)
		return items
		
