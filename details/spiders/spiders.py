import scrapy
import get_url
from scrapy import Selector
from readability import Document

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

    def start_requests(self):

        urls = [
            'http://eei.sjtu.edu.cn/Show.aspx?info_id=356&info_lb=571&flag=490',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = '%s.html' % id[1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # sel = Selector(response)
        # content = sel.xpath('//div[@class="arc-body font14"][2]/p[1]')

        doc = Document(response.body)
        doc.title()
        print 'doc.title()', doc.title()