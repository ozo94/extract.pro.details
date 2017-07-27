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

        for x in cache:
            # 去除ajax代码,使用clean_html时候可以忽略这些步骤
            if '$' in x:
                x = ''
            else:
                x = x.replace('\t','').replace(' ', '').\
                    replace('\n', '').replace('\r', '')

            if x:
                result.append(x)

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
    s = file('../../test.html').read()
    data = open('result1.txt', 'w')

    code = get_code(s)

    result = FilterTag.strip_tags(s.decode(code))
    print result
    data.write(result)

