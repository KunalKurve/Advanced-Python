#Scrapy Code


import scrapy
import time
import requests
from scrapy.http import Response

class MovieSpider(scrapy.Spider):
    name='awards'
    start_urls=['https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture']

    def _parse(self,response):
        # data={}
        # data['title'] = response.css("tittle::text").extract()
        # yield data
        #if error install : pip install twisted==22.10.0

        for ln in response.css(r"tr[style='background:#FAEB86'] a[href*='film']::attr('href')").extract():
            url =response.urljoin(ln)
            print(url)
            req = scrapy.Request(url, callback=self.parse_titles)
            time.sleep(5)
            yield req

    def parse_titles(self, response):
        for sel in response.css('html').extract():
            data ={}
            data['title']=response.css(r"h1[id='firstHeading'] i::text").extract()
            #data['title']=response.xpath(r"//*[id='firstHeading'] i::text").extract() can use this instead of above line
            data['directedby']=response.css(r"tr:contains('Directed by') a[href*='/wiki/']::text").extract()
            #data['starrring']=------
            data['releasedate']=response.css(r"tr:contains('Release dates') li::text").extract()
            yield data


