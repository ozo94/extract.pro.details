# coding=utf-8
import re


# 手工匹配的方法，存在考虑不到的情况（主要使用正则表达式去匹配）
# 这个方法的好处是，不用考虑编码问题，原网页是什么编码，还返回什么编码
def filter_tags(htmlstr):
    '''
    过滤HTML中的标签
    将HTML中标签等信息去掉
    :param htmlstr: HTML字符串.
    :return:
    '''



    # 先过滤CDATA, 匹配CDATA
    re_cdata = re.compile('//<!CDATA\[[ >]∗ //\] > ',re.I)
    # Script
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    # style
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
    # 处理换行
    re_br = re.compile('<br\s*?/?>')
    # HTML标签
    re_h = re.compile('</?\w+[^>]*>')
    # HTML注释
    re_comment = re.compile('<!--[^>]*-->')
    # 一些非标准的标签，所有<test>格式都去除，暴力方案
    re_all = re.compile('<[^>]+>')



    # 去掉对应的内容
    s = htmlstr



    s= re_all.sub('',s)
    s = re_cdata.sub('', s)
    s = re_script.sub('', s)
    s = re_style.sub('', s)
    s = re_h.sub('', s)
    s = re_comment.sub('', s)
    s = re_br.sub('', s)

    # 去掉多余的空行,换行就暂不去除了，原网页相当于分好换行了
    blank_line_l = re.compile('\n')
    s = blank_line_l.sub('', s)
    blank_kon = re.compile('\t')
    s = blank_kon.sub('', s)
    blank_two = re.compile('\r')
    s = blank_two.sub('', s)
    # blank_three = re.compile(' ')
    # s = blank_three.sub('', s)

    # 替换实体
    s = replaceCharEntity(s)
    return s



def replaceCharEntity(htmlstr):
    '''
    替换常用HTML字符实体.
    使用正常的字符替换HTML中特殊的字符实体.
    你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
    :param htmlstr: HTML字符串
    :return:
    '''
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"''"', '34': '"', }

    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称，如>
        key = sz.group('name')  # 去除&;后entity,如>为gt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def repalce(s, re_exp, repl_string):
    return re_exp.sub(repl_string,s)


if __name__ == '__main__':
    s = file('../../tmp/clean_html.html').read()
    data = open('../test/result_re.txt', 'w')
    result = filter_tags(s)
    print result
    data.write(result)
