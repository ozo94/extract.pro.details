# coding=utf-8
import re


def get_result(str ,result, tags, ids):

    # 对应文本的所属专家id和名字
    id_list = []
    for x in ids:
        id = x.strip('\n').split(';')
        id_list.append([id[0], id[1], id[2]])

    flag = 0
    for x in str:
        x = x.strip('\n')
        id = id_list[flag]
        flag = flag+1

        setence = x.split('。')

        for x in setence:
            x = x.strip(' ').strip('\n')
            data = ' '.join(x.split())
            print data
            if data:
                result.write(data+'\n')
                tags.write(id[0] + ' ' + id[1]+ ' '+ id[2] +'\n')


if __name__ == '__main__':
    str = open('../tmp/contents.txt', 'r')
    id = open('../tmp/tags.txt', 'r')

    result = open('../data/selected_mess/sentences/sentences.txt', 'w')
    tags = open('../data/selected_mess/sentences/tags.txt', 'w')


    get_result(str, result, tags, id)