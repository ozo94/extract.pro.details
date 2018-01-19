# coding=utf-8
'''
    网页编码识别
    去除js代码、style格式
'''

import chardet

def get_code(data):
    '''
    编码预测，这个方法会读取所有的数据流后做出判断
    高级用法: http://chardet.readthedocs.io/en/latest/usage.html
    :param data:
    :return:
    '''
    result = chardet.detect(data)
    print result
    return result['encoding']

def del_code(data):
    '''
    去除js代码，注释文件
    :param data:
    :return:
    '''
    attr_lists = ['$(', 'var', '//', '<!']
    for attr in attr_lists:
        if attr in data:
            return False

    return True