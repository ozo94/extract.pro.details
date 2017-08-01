# coding=utf-8
import sys

import scrapy
from readability import Document

from details.selected_mess import get_url, remove_bs, remove_pas


reload(sys)
sys.setdefaultencoding('utf-8')



datas = get_url.URLS
p_name = {}
urls = []

for data in datas:
    urls.append(data[2])
    p_name[data[2]]= [data[0], data[1]]

fp = open('tmp/result.txt', 'w')
tags = open('tmp/tags.txt', 'w')
result = open('result/result.txt', 'w')


class DSpider(scrapy.Spider):
    name = "Details"

    # 这两个默认生成的函数的参数没法随意修改的
    def start_requests(self):

        # urls = [
        #     'http://www.sjtuirc.sjtu.edu.cn/Person1/wangrz.htm',
        # ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'tmp/%s.html' % 'test'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


        # 使用readability包的初步处理，由于网页格式的问题（网页不规范），效果并不理想
        doc = Document(response.body)
        clean_html, title = self.get_cleanpage(doc)


        # 使用htmlpaser,仍然存在问题(配合readablity来完成基本的抽取)
        data = remove_pas.FilterTag.strip_tags(clean_html)
        # data = remove_bs.get_thml_content(clean_html)
        if data :
            # 获取对应专家的信息
            key = response.url
            str_data = data
            fp.write(str_data + '\n')
            tag_data = str(p_name[key][0]) + ';'+ p_name[key][1]
            tags.write(tag_data + '\n')





    def get_cleanpage(self, doc):

        # 爬去网页大体信息（字节大小，请求数等）
        summary = doc.summary()

        # 遇到错误 gbk转码过程中某些字符没法转码，直接使用空格替换掉
        # 返回utf-8标准网页（去头去尾），在某些网页中可能会
        clean_html = doc.get_clean_html().replace(u'\xa0', u' ')

        # 读取body部分的数据，但是中文不见了，变成了奇怪的编码
        content = doc.content()

        # 获得标题
        short_title = doc.short_title()
        title = doc.title()

        with open('tmp/clean_html.html', 'wb') as f:
            f.write(clean_html)

        with open('tmp/content.html', 'wb') as f:
            f.write(content)
        return clean_html, title
