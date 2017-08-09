# coding=utf-8
import re
import string

def remove_qoutes(data):
    # （1）去除英文符号,英文不需要转码
    # data = data.translate(None, string.punctuation)
    for qoute in string.punctuation:
        data = data.replace(qoute, ' ')


    # （2）去除中文的符号
    # 直接用re.sub，文本内容会破相（中文字符会破开，变成乱码），首先需要进行转码
    data = data.decode('utf-8')
    data = re.sub("[——！，。？、￥%……&*（）：；【】“”‘’《》～　◆]+".decode('utf-8'), ' ', data)
    # data = re.sub("[！？￥%……&*【】《》：]+".decode('utf-8'), ' ', data)
    # print data

    return data.encode('utf-8')

def remove_en(data):
    '''
    去除文本中的英文
    :param data:
    :return:
    '''
    data = re.sub('[a-zA-Z\.]+', ' ', data)
    # print data
    return data

def optimization(data):
    '''
    进一步规范文本内容，保留一定量的基本符号，去除特殊字符
    :return:
    '''
    data = re.sub("[！？￥……&【】　◆]+".decode('utf-8'), ' ', data)

    # 去除单个的英文，或者数字（一般都是序号）
    result = []
    datas = data.split(' ')
    for data in datas:
        pass


if __name__ == '__main__':
    datas = open('../data/sentences/sentences.txt', 'r')
    clean_ch = open('../data/sentences/clean_ch.txt', 'w')

    for data in datas:
        data = data.strip('\n')

        data = remove_qoutes(data)
        data = remove_en(data)

        data = ' '.join(data.split()).strip(' ')
        if  data == '':
            data = '0'
        # print data
        clean_ch.write(data+ '\n')

