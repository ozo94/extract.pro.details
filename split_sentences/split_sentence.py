# coding=utf-8
import re
import choose_data


def get_result(str ,result, tags, ids, MIN_LEN, MAX_LEN, num ):
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
        # print 'content:', content
        # print flag
        id = id_list[flag]
        flag = flag+1

        setence = re.split('。|；', content)

        for datas in setence:
            # 判断句子中是否有足够多的中文字符

            if datas and choose_data.judge_sentence(datas, MIN_LEN):
                datas = choose_data.optimization(datas)
            else:
                continue


            # 句子过长时，考虑对句子分解
            if len(datas) > MAX_LEN:
                # print datas
                num += 1
            #     datas = re.split('，', datas)
            #     for data in datas:
            #         result.write(data.strip(' ') + '\n')
            #         tags.write(id[0] + ' ' + id[1] + ' ' + id[2] + '\n')

            result.write(datas.strip(' ') + '\n')
            tags.write(id[0] + ' ' + id[1] + ' ' + id[2] + '\n')

    print 'long sentences: ', num


if __name__ == '__main__':
    str = open('../data/tmp/contents.txt', 'r')
    id = open('../data/tmp/tags.txt', 'r')

    result = open('../data/sentences/sentences.txt', 'w')
    tags = open('../data/sentences/tags.txt', 'w')


    get_result(str, result, tags, id, 20, 200, 0)
