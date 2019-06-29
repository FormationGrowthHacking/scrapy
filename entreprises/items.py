# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field



class EntreprisesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Camps d'enthreprises
    startup_name= Field()
    startup_date_creation=Field()
    startup_website=Field()
    startup_email=Field()
    startup_address=Field()
    startup_founders=Field()
    startup_market=Field()
    startup_description=Field()
    startup_short_description=Field()
    
    #champs de controle
    url= Field()
    project=Field()
    spider=Field()
    server=Field()
    date=Field()
    
    