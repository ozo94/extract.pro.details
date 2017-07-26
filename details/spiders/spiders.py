# coding=utf-8
import scrapy
import get_url
from scrapy import Selector
from readability import Document

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



datas = get_url.URLS
p_name = []
urls = []
id = []
for data in datas:
    urls.append(data[2])
    p_name.append(data[1])
    id.append(data[0])


class DSpider(scrapy.Spider):
    name = "Details"

    # 这两个默认生成的函数的参数没法随意修改的
    def start_requests(self):

        urls = [
            'http://www.sjtuirc.sjtu.edu.cn/Person1/wangrz.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = '%s.html' % 'test'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # sel = Selector(response)
        # content = sel.xpath('//div[@class="arc-body font14"][2]/p[1]')
        doc = Document(response.body)
        # print 'type(doc)', type(doc)
        self.get_cleanpage(doc)


    def get_cleanpage(self, doc):

        # 爬去网页大体信息（字节大小，请求数等）
        summary = doc.summary()

        # 遇到错误 gbk转码过程中某些字符没法转码，直接使用空格替换掉
        clean_html = doc.get_clean_html().replace(u'\xa0', u' ')

        # 读取body部分的数据，但是中文不见了，变成了奇怪的编码
        content = doc.content()

        # 获得标题
        short_title = doc.short_title()
        title = doc.title()

        data = doc
        with open('content.html', 'wb') as f:
            f.write(clean_html)