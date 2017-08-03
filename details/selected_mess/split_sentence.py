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
            # 去除多余空格
            x = x.strip(' ')
            data = ' '.join(x.split())
            if data:
                result.write(data+'\n')
                tags.write(id[0] + ' ' + id[1]+ ' '+ id[2] +'\n')
            print data


if __name__ == '__main__':
    str = open('../../tmp/result.txt', 'r')
    id = open('../../tmp/tags.txt', 'r')

    result = open('../result/result.txt', 'w')
    tags = open('../result/tags.txt', 'w')


    get_result(str, result, tags, id)