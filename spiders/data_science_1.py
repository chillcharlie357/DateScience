import scrapy
from selenium import webdriver
from item import WangyiproItem
class ZhengWuSpider(scrapy.Spider):

    name = 'ZhengWu'

    start_urls = ['https://news.163.com/']
    models_urls = []#存储五个相应模块的url
    #解析模块

    #实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=)

    def parse(self,response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[2]/div[2]/div[2]/div[2]/div/ul')
        alist = [3,4,6,7,8]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

        #依次对详情页进行请求
        for url in self.models_urls:#对每一个url经行发出请求
            yield scrapy.Request(url , callback=self.parse_model)

    #每一个详情页都是动态加载出来的
    def parse_model(self,response):#解析每一个板块中对应新闻的标题和新闻详情页的url
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            news_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url = news_detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        content = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]').extract()
        content = ''.join(content)
        item = response.mata['item']
        item['content'] = content

        yield item
    def closed(self,spider):
        self.bro.quit()
