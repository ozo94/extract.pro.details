# coding=utf-8


def get_entitys(row_ch):
    '''
    统计中文字符串中，对应实体的种类和个数（ch.txt文件中给出了sentences中每行包含的实体名）
    :param row_ch: ch.txt中对应行的所有实体名（通过斯坦福coreNLP中文模型工具，逐行分析，结果存入ch.txt文件中去）
    :return: 返回对应行，实体种类以及统计的数目
    '''
    entitys = []
    count = {}
    ch_alls = row_ch.strip().split(' ')

    for entity in ch_alls:
        if entity not in entitys:
            entitys.append(entity)
            count[entity] = 1
        else:
            count[entity] += 1

    return entitys, count


def judge_absent(row_content, category):
    '''
    判断缺省某个实体后，需要满足的额外条件
    :param row_content: sentences中对应的行（文本）
    :param category: 额外规则种类（对应txt文本匹配词）
    :return:
    '''
    rex = open('../data/rule/'+category+'_absent.txt', 'r')

    for token in rex:
        token = token.strip('\n')
        if token in row_content:
            return True

    return False

def judge_all(row_content, category , mode = 'all'):
    '''
    对文本应该先进行先验判断，某些词至少含有一个，或者某些词一次都不能出现
    :param row_content:
    :param category:
    :param mode: 3种模式:contain,no_contain,all
    :return:
    '''
    contain, not_contain = 0 , 1

    rex_c = open('../data/rule/'+category+'_contain.txt', 'r')
    rex_n = open('../data/rule/'+category+'_notC.txt', 'r')

    for token in rex_c:
        token = token.strip('\n')
        if token in row_content:
            contain  = 1
            break

    for token in rex_n:
        token = token.strip('\n')
        if token in row_content:
            not_contain = 0
            break

    if mode == 'contain':
        return contain
    if mode == 'not_contain':
        return not_contain
    if mode == 'all':
        return contain and not_contain


def match_rule(row_content, rules, entitys, count, category, mode):
    '''
    判断当前的句子符不符合规则，返回boolean值
    :param rules: 规则：实体种类、每类个数范围，career = {'ORGANIZATION': [1,10], 'DATE': [0,5], 'TITLE':[1,5], 'PERSON': [0,1]}
    :param entitys:
    :param count:
    :return:
    '''

    # 先验判断
    if not judge_all(row_content, category, mode):
        return False

    # 实体判断，缺省处理
    for rule in rules.keys():
        # 包含规则内的实体，是否满足范围
        if rule in entitys:
            if count[rule] < rules[rule][0] or count[rule] > rules[rule][1]:
                return False
        # 规则内要求的实体不存在时，看看该实体能否为0
        else:
            if rules[rule][0] > 0:
                return False
            else:
                return judge_absent(row_content, category)


    return True


def give_sentences(rule, category, mode, fp):
    """
    返回满足规则的句子，写到fp文件中去
    :param rule: 给定的规则
    :param category: 规则种类
    :param mode: 选择先验模式
    :param fp:
    :return:
    """
    ch = open('../data/entities/ch.txt', 'r')
    ch_lines = ch.readlines()

    result = open('../data/sentences/sentences.txt', 'r')
    result_lines = result.readlines()

    tags = open('../data/sentences/tags.txt', 'r')
    tags_lines = tags.readlines()

    lines = []
    rows = len(ch_lines)


    # 逐行读取，将满足规则句子所在行号记录下来（entitys[0]记录的就是行号，从1开始）
    for i in range(rows):
        entitys, count = get_entitys(ch_lines[i])
        row_content = result_lines[i].strip('\n')
        if match_rule(row_content, rule, entitys, count, category, mode):
            lines.append(int(entitys[0]))


    # 将对应条目写到一行里面
    flag = ''
    for line in lines:
        data = result_lines[line - 1].strip('\n')
        print data.strip('\n')
        tag = tags_lines[line - 1].split(' ')
        name = tag[0]
        college = tag[1]
        company = tag[2].strip('\n')

        if flag == name:
            fp.write( data.strip('\n') + '。')
        else:
            flag = name
            fp.write('\n'+ flag+ ','+ college+','+ company+ ',')
            fp.write(data.strip('\n') + '。')

    return lines


if __name__ == "__main__":

    career_csv = open('../data/final_result/career.csv', 'w')
    contribute_csv = open('../data/final_result/contribute.csv', 'w')
    area_csv = open('../data/final_result/area.csv', 'w')

    career = {'ORGANIZATION': [1,10], 'DATE': [1,5], 'TITLE': [0,2], 'PERSON': [0,0] }
    contribute = {'ORGANIZATION': [1,10],  'DATE':[0,2]}
    area = {'O':[2,20]}


    give_sentences(career, 'career', 'not_contain', career_csv)
    # give_sentences(contribute, contribute_csv)
    # give_sentences(ch, area, area_csv)










