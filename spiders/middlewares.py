from scrapy import signals
from scrapy.http import HtmlResponse
from time import sleep
class DownloaderMiddleWare(object):
    def process_response(self,request,response,spider):
        bro = spider.bro
        if request.url in spider.models_urls:
            bro.get(request.url)
            sleep(3)
            page_text = bro.page_source
            #response:对应的响应对象
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response
        else:
            #response：非对应的相应对象
            return response