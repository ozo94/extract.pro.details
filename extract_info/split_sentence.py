# coding=utf-8
import re


def get_result(str ,result, tags, ids, MIN_LEN ,MAX_LEN):
    '''
    对原始文本断句，建立新的文档（txt）
    :param str: 原始文本
    :param result: 断完句后的新文本
    :param tags: 新文本的映射表（每行对应哪个专家信息）
    :param ids: 旧文本映射表
    :param MIN_LEN: 断句后，每句的最小长度，不满足就抛弃该句
    :param MAX_LEN: 断句后，每句的最大长度
    :return:
    '''

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
            if len(datas) > MIN_LEN:
                print datas
                # 句子过长时，考虑对句子分解
                if len(datas) > MAX_LEN:
                    datas = re.split('，|、', datas)
                    for data in datas:
                        # 分解失败，去除
                        if len(data) < MAX_LEN:
                            result.write(data.strip(' ') + '\n')
                            tags.write(id[0] + ' ' + id[1] + ' ' + id[2] + '\n')
                else:
                    result.write(datas.strip(' ') + '\n')
                    tags.write(id[0] + ' ' + id[1] + ' ' + id[2] + '\n')



if __name__ == '__main__':
    str = open('../tmp/contents.txt', 'r')
    id = open('../tmp/tags.txt', 'r')

    result = open('../data/sentences/sentences.txt', 'w')
    tags = open('../data/sentences/tags.txt', 'w')


    get_result(str, result, tags, id, 20, 100)
