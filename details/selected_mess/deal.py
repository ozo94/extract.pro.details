# coding=utf-8
import re



def get_result(str ,result, tags, ids):

    id_list = []
    for x in ids:
        id = x.strip('\n').split(';')
        id_list.append([id[0], id[1]])

    flag = 0
    for x in str:
        id = id_list[flag]

        # 信息抽取，正则匹配信息
        # basic = re.compile(r'；')
        # order = re.compile('\d{1,2}\.\s*')
        # column = re.compile(r'\s+[\u4e00-\u9fa5]+\s{0,1}：')

        # 用指定的分割符来实现句子的分割
        # x = basic.sub('。', x)
        # x = order.sub('。', x)
        # x = column.sub('。', x)
        # print x
        # setence = re.split(r'。|；|;|\s+[\u4e00-\u9fa5]+\s*:\s*|：|\s+\d{1,2}\.\s+', x)

        setence = x.split('。')


        for x in setence:
            # 去除多余空格
            x = x.strip(' ')
            data = ' '.join(x.split())

            result.write(data+'\n')
            tags.write(id[0] + ' ' + id[1]+ '\n')
            print data

if __name__ == '__main__':
    str = open('../../tmp/result.txt', 'r')
    id = open('../../tmp/tags.txt', 'r')

    result = open('../result/result.txt', 'w')
    tags = open('../result/tags.txt', 'w')

    str = open('../data/result_re.txt', 'r')

    get_result(str, result, tags, id)