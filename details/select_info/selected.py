def get_entitys(str):
    entitys = []
    alls = str.strip().split(' ')
    for entity in alls:
        if entity not in entitys:
            entitys.append(entity)

    return entitys

def rule(rules, entitys, confidence):
    flag = 0
    for rule in rules:
        if rule  in entitys:
            flag = flag+1
    if flag >= confidence:
        return True
    else:
        return False

if __name__ == "__main__":
    path = '../data/paser.txt'
    paser = open(path, 'r')
    fp = open('../data/career.txt', 'w')

    career = ['ORGANIZATION', 'DATE', 'TITLE']

    lines = []
    for x in paser:
        entitys = get_entitys(x)
        if rule(career, entitys, 2):
            print entitys[0]
            lines.append(int(entitys[0]))

    result = open('../data/result.txt', 'r')
    result_lines = result.readlines()

    tags = open('../data/tags.txt', 'r')
    tags_lines = tags.readlines()

    for line in lines:
        data = result_lines[line]
        tag = tags_lines[line].split(' ')[1]







