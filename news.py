#import libraries
import random
import scrapy
from scrapy.crawler import CrawlerProcess
import json

#crawler class to extarct link of articles 
class IPLSpider(scrapy.Spider):
    name = "IPL"
    start_urls = [
      'https://www.iplt20.com/news'
    ]
    docID =1
    
   

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    user_agent =user_agent_list[random.randint(0,len(user_agent_list)-1)]
    
    #parsing the starturl to extract article links
    def parse(self, response):
        for sel in response.xpath('//ul[@class="content-grid flex-grid u-negative-margin"]/li[@class="content-grid__item col-3 col-4-tab col-12-phab"]'):
            link = sel.xpath('a/@href').extract()
            for i in link:
                url = 'https://www.iplt20.com'+i
                yield scrapy.Request(url, callback = self.parse_dir_contents)
    
    #parsing article to extract url,title,content 
    def parse_dir_contents(self, response):
        para = response.xpath('//div[@class="main-article__body main-article__wrapper wrapper js-article-body"]')
        text = para.xpath('.//p//text()').getall()
        title = response.xpath("//head//title/text()").extract()
        url = response.url
        scraped_info = {
            'id':self.docID,
            'title' : title,
            'url' : url,
            'text' : text,
            }
            
        with open('Documents/document'+str(self.docID)+'.json', 'w') as json_file:
            json.dump(scraped_info, json_file, indent= 4)
        self.docID+=1
            
            
            
#creating crawler object to crawl url       
process = CrawlerProcess()
process.crawl(IPLSpider)
process.start()

      
    
        









