#! /usr/bin/python
# -*- coding:utf-8 -*-

import re
from HTMLParser import HTMLParser

# 使用该方法时，编码存在很大的问题（不同的网站，编码不一样，paser执行的时候有转码要求）
# import sys
# reload(sys)
# sys.setdefaultencoding('gb2312')


class FilterTag():
    def __init__(self):
        pass


    def strip_tags(self, htmlStr):
        '''
        使用HTMLParser进行html标签过滤
        :param htmlStr:
        '''
        self.htmlStr = htmlStr
        cache = []
        result = []

        parser = HTMLParser()
        parser.handle_data = cache.append
        parser.feed(htmlStr)
        parser.close()

        for x in cache:
            # 去除ajax代码
            if '$' in x:
                x = ''
            else:
                x = x.replace('\t','').replace(' ', '').replace('\n', '')
            if x:
                result.append(x+'\n')

        return ''.join(result)

    def stripTagSimple(self, htmlStr):
        '''
        最简单的过滤html <>标签的方法    注意必须是<任意字符>  而不能单纯是<>
        :param htmlStr:
        '''
        self.htmlStr = htmlStr
        dr =re.compile(r'<[^>]+>',re.S)
        # dr = re.compile(r']*>', re.S)
        htmlStr = re.sub(dr, '', htmlStr)
        return htmlStr


if __name__ == '__main__':
    s = file('D:/spider_code/details/content.html').read()
    filters = FilterTag()
    data = open('result1.txt', 'w')
    result = filters.strip_tags(s)
    print result
    data.write(result)
