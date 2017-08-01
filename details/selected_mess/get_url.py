# coding=utf-8
import pandas as pd

# 只是基于当前目录的文件相对目录
# fp = pd.read_csv('../data/url_t1.csv')

# 引用这个模块时，爬虫的起始处理路径为整个项目的根目录
# fp = pd.read_csv('details/data/url_t1.csv')
fp = pd.read_csv('details/data/zdh_TH.csv')


URLS = []
id = 0

for data in fp.iterrows():
    name = data[1][3].replace(' ', '')
    url =  data[1][0]
    if not pd.isnull(url):
        URLS.append([id,name,url])
        id = id + 1
        # print name, url
