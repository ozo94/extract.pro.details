# coding=utf-8
import re
from choose_zh import remove_qoutes


def get_result(str ,result, tags, ids):

    # 对应文本的所属专家id和名字
    id_list = []
    for x in ids:
        id = x.strip('\n').split(';')
        id_list.append([id[0], id[1], id[2]])

    flag = 0
    for content in str:
        content = content.strip('\n')
        print 'content:', content
        id = id_list[flag]
        flag = flag+1

        setence = re.split('。|；', content)

        for datas in setence:
            datas = ' '.join(datas.strip(' ').split(' '))
            if datas:
                print datas
                if len(datas)> 120:
                    datas = re.split('，|、', datas)
                    for data in datas:
                        result.write(data.strip(' ') + '\n')
                        tags.write(id[0] + ' ' + id[1] + ' ' + id[2] + '\n')
                else:
                    result.write(datas.strip(' ') + '\n')
                    tags.write(id[0] + ' ' + id[1] + ' ' + id[2] + '\n')

            # # 空格分割，句子结尾处可能并没有符号
            # # ' 1987 年 毕业...' 解决每个属性过短的情况
            # datas = datas.split(' ')
            #
            # # 五个中文字符的长度为15
            # row = ''
            # for data in datas:
            #     data = data.strip(' ')
            #     if len(data)>15:
            #         row += data
            #         print row.strip(' ')
            #         result.write(row.strip(' ') + '\n')
            #         tags.write(id[0] + ' ' + id[1] + ' ' + id[2] + '\n')
            #         row = ' '
            #     else:
            #         row += data




if __name__ == '__main__':
    str = open('../tmp/contents.txt', 'r')
    id = open('../tmp/tags.txt', 'r')

    result = open('../data/sentences/sentences.txt', 'w')
    tags = open('../data/sentences/tags.txt', 'w')


    get_result(str, result, tags, id)