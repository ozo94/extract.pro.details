# coding=utf-8
import os
from scrapy import cmdline


# 生成对应的文件夹
filename = ['final_result', 'sentences', 'source_data', 'tmp']
if not os.path.exists('data/'):
    os.mkdir('data/')

for file in filename:
    if not os.path.exists('data/'+file):
        os.mkdir('data/'+file)

# 运行爬虫
cmdline.execute('scrapy crawl Details'.split(' '))

