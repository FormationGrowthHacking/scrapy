import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider (scrapy.Spider):
    #définition de votre spider
    
    pass
    
    


process=CrawlProcess({'USER_AGENT':'Mozilla/5.0(compatible;MSIE 7.0; Windows NT 5.1)'})
process.crawl(MySpider)
process.start()
#le script va être bloqué ici jusqu'à ce que le crawling soit faite et terminée

