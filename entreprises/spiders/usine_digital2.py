# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.response import open_in_browser


def parse_details(self,response):
    if "item_name" not in response.body:
        open_in_browser(response)
        
    item=response.mega.get('item',None)
    if item:
        return item
    else:
        self.logger.warning("pas d'item reçu pour %s", response.url)
        
        
        

class UsineDigital2Spider(CrawlSpider):
    name = 'usine-digital2'
    allowed_domains = ['usine-digitale.fr']
    start_urls = ['https://www.usine-digitale.fr/annuaire-start-up/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//*[@rel='next']")),
        Rule(LinkExtractor(restrict_xpaths="//*[@itemprop='url']"),
             callback='parse_item')
    )

    def parse_item(self, response):
        i = {}    
        
        i["startup_name"] = response.xpath("//h1/text()").extract()
        i["startup_date_creation"] = response.xpath("//*[@itemprop='foundingDate']/@content").extract()
        i["startup_website"] = response.xpath ("//*[@id='infoPratiq']//a/@href").extract()
        i["startup_email"] = response.xpath ("//*[@itemprop='email']/text()").extract()
        i["startup_address"] = response.xpath ("//*[@id='infoPratiq']//p/text()").extract()
        i["startup_founders"] = response.xpath ("//*[@itemprop='founders']/p/text()").extract()
        i["startup_market"] = response.xpath ("//*[@id='ficheStartUp']/div[1]/article/div[6]/p").extract()
        i["startup_description"] = response.xpath ("//*[@itemprop='description']/p/text()").extract()
        i["startup_short_description"] = response.xpath ("//*[@itemprop='review']/p").extract()
        
        return i
