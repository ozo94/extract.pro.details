#! /usr/bin/python
# -*- coding:utf-8 -*-
'''
    使用该方法时，编码存在很大的问题（不同的网站，编码不一样，paser执行的时候有转码要求）
'''

from HTMLParser import HTMLParser
from data_sel import del_code

class FilterTag():
    def __init__(self):
        pass

    @staticmethod
    def strip_tags(htmlStr):
        '''
        使用HTMLParser进行html标签过滤
        :param htmlStr:
        '''
        cache = []
        result = []

        parser = HTMLParser()
        parser.handle_data = cache.append
        parser.feed(htmlStr)
        parser.close()

        for data in cache:
            data = data.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
            # 去除英文双引号，单引号代替，作为或许文本分割特征
            data = data.replace('"',  "'")
            if data.strip() and del_code(data):
                result.append(data.strip(' '))

        return ' '.join(result)


