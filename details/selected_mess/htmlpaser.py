#! /usr/bin/python
# -*- coding:utf-8 -*-

import re
from HTMLParser import HTMLParser
import chardet


# 使用该方法时，编码存在很大的问题（不同的网站，编码不一样，paser执行的时候有转码要求）
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 编码预测
def get_code(data):
    # 这个方法会读取所有的数据流后做出判断
    result = chardet.detect(data)
    print result
    return result['encoding']

    # 高级用法: http://chardet.readthedocs.io/en/latest/usage.html


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
            data = data.replace('\t','').replace('\n', '').replace('\r', '')

            if data:
                result.append(data+ ' ')

        return ''.join(result)



if __name__ == '__main__':
    s = file('../../tmp/clean_html.html').read()
    data = open('../data/selected_mess/test/htmlpas.txt', 'w')

    code = get_code(s)

    result = FilterTag.strip_tags(s.decode(code))
    print result
    data.write(result)

