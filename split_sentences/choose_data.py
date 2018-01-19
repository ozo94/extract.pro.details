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
    data = re.sub("[——！，。？、￥%……&*（）：；【】“”‘’《》～　◆│]+".decode('utf-8'), ' ', data)
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

def remove_num(data):
    '''
    去除文本中的数字
    :param data:
    :return:

    '''
    data = re.sub('\d+', ' ', data)
    return data

def judge_sentence(data, LEN):
    '''
    判断句子中是否含有所需要的足够量的中文文本（至少7个汉字）
    :param data:
    :return:
    '''
    data = remove_qoutes(data)
    data = remove_en(data)
    data = remove_num(data)
    data = ''.join(data.strip().split())

    if len(data) > LEN:
        return True
    else:
        return False

def optimization(data):
    '''
    进一步规范文本内容，保留一定量的基本符号，去除特殊字符
    :return:
    '''

    data = ' ' + data
    # 去除特殊字符
    data = data.decode('utf-8')
    data = re.sub("[！？￥……&【】　◆*]+".decode('utf-8'), '', data)

    # 规范年月
    data = re.sub('（(年|月|日)）'.decode('utf-8'), '', data)
    data = re.sub('\s+(年|月|日)'.decode('utf-8'), r'\1', data)
    data = re.sub('\s+(～|—)'.decode('utf-8'), r'\1', data)
    data = re.sub('(～|—)\s+'.decode('utf-8'), r'\1', data)
    data = re.sub('(年)\s+(\d+)'.decode('utf-8'), r'\1\2', data)

    data = data.encode('utf-8')
    data = re.sub('\s+(\/|\-|\~)', r'\1', data)
    data = re.sub('(\/|\-|\~)\s+', r'\1', data)

    # 去除序号
    data = re.sub("((\(|\[|\{|（)\s*\d{1,2}\s*(\)|\]|\}|）)|\s+\d{1,2}\s*(\.|．|、))", '', data)

    # 去除单个的英文噪声
    data = re.sub('\s+[a-zA-Z]{1}\s+', '', data)

    # 去除多余空格
    # data = re.sub('(\w{1})\s+(\w{1})', r'\1。\2', data)
    data = ' '.join(data.strip().split())

    return data


if __name__ == '__main__':
    datas = open('../data/sentences/sentences.txt', 'r')
    clean_ch = open('../data/sentences/clean_ch.txt', 'w')

    for data in datas:
        data = data.strip('\n')

        data = remove_qoutes(data)
        data = remove_en(data)

        data = ' '.join(data.split()).strip(' ')
        if  data == '' or len(data) > 200:
            data = '0'
        # print data
        clean_ch.write(data+ '\n')


