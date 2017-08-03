# coding=utf-8

# 统计中，英文字符串中的对应实体的种类和个数
def get_entitys(ch, en):
    entitys = []
    count = {}
    ch_alls = ch.strip().split(' ')
    en_alls = en.strip().split(' ')

    for entity in ch_alls:
        if entity not in entitys:
            entitys.append(entity)
            count[entity] = 1
        else:
            count[entity] += 1

    for entity in en_alls:
        if entity not in entitys:
            entitys.append(entity)
            count[entity] = 1
        else:
            count[entity] += 1

    return entitys, count

# 当前的句子符不符合规则
def match_rule(rules, entitys, count):

    for rule in rules.keys():
        if rule  in entitys:
            if count[rule] <= rules[rule][0] and count[rule] >= rules[rule][1]:
                return False
        else:
            return False

        return True


# 中文，英文的词性分析在一起参考
def give_sentences(ch, en, career, fp):
    lines = []
    ch_lines = ch.readlines()
    en_lines = en.readlines()
    rows = len(ch_lines)+1

    for i in range(rows):
        entitys, count = get_entitys(ch_lines[i], en_lines[i])
        if match_rule(career, entitys, count):
            # 返回行号，在txt文本中以 1 开始的
            lines.append(int(entitys[0]))

    result = open('../result/result.txt', 'r')
    result_lines = result.readlines()

    tags = open('../result/tags.txt', 'r')
    tags_lines = tags.readlines()

    flag = ''
    for line in lines:
        data = result_lines[line - 1]
        print data
        tag = tags_lines[line - 1].split(' ')
        name = tag[0]
        college = tag[1]
        company = tag[2]

        if flag == name:
            fp.write( data.strip('\n') + '。')
            # print sentences
        else:
            flag = name
            fp.write('\n'+ flag+ ','+ college+','+ company+ ',')
            sentences = ''



if __name__ == "__main__":
    ch = open('../data/ch.txt', 'r')
    en = open('../data/en.txt', 'r')
    career_csv = open('../data/career.csv', 'w')
    contribute_csv = open('../data/contribute.csv', 'w')
    area_csv = open('../data/area.csv', 'w')

    career = {'ORGANIZATION': [1,10], 'DATE': [1,2], 'TITLE':[1,3], 'PERSON': [0,1]}
    contribute = {'ORGANIZATION': [1,10], 'ORDINAL':[0,2], 'DATE':[0,2], 'PERSON': [0,1]}
    article = {}
    area = {'O':[2,20]}

    # give_sentences(ch, en, career, career_csv)
    give_sentences(ch, en, contribute, contribute_csv)
    give_sentences(ch, en, area, area_csv)










