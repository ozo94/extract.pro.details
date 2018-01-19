# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from readability import Document
from details.spiders import get_url
from page_content import htmlpaser, beatifulsoup
from page_content.data_sel import get_code
import os


# 获得专家的名字，学校，学院，个人主页这四种信息
urls = get_url.URLS
pro_lists = get_url.pro_lists
# 存储html信息
source_html = 'data/source_data/source_html'
clean_html = 'data/source_data/clean_html'
html_content = open('data/source_data/contents/contents.txt', 'w')


class DSpider(scrapy.Spider):
    name = "Details"

    # 这两个默认生成的函数的参数没法随意修改的
    def start_requests(self):
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # response.body(str)与reponse.text(unicode)的区别使用
        # 注意页面的编码问题
        key = response.url
        code = get_code(response.body)
        text = response.body.decode(code).encode('utf-8')
        name, college = pro_lists[key][0], pro_lists[key][1]

        # 存储原始格式的html文件
        homepage_name = unicode(name+ '_' + college, 'utf-8')
        filename = '%s.html' % homepage_name
        with open(os.path.join(source_html, filename), 'w') as f:
            f.write(text)
        self.log('Saved origin file %s' % filename)

        # 使用readability包的初步处理,获取较为干净的页面
        doc = Document(text)
        clean_text, title = self.get_cleanpage(doc)
        with open(os.path.join(clean_html, filename), 'w') as f:
            f.write(clean_text)
        self.log('Saved clean file %s' % filename)

        # 使用htmlpaser,抽取所有的文字(配合readablity来完成基本的抽取)
        data = htmlpaser.FilterTag.strip_tags(text)
        data1 = beatifulsoup.get_html_content(text)
        html_content.write(homepage_name + ': "' + data + '"\n')

    def get_cleanpage(self, doc):
        '''
        summary:网页大体信息（字节大小，请求数等）
        clean_html:网页纯文本
        :param doc:
        :return:
        '''
        summary = doc.summary()
        clean_html = doc.get_clean_html().replace(u'\xa0', u' ')
        content = doc.content()
        short_title = doc.short_title()
        title = doc.title()

        return clean_html, title
