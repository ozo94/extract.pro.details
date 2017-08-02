def get_entitys(str):
    entitys = []
    alls = str.strip().split(' ')
    for entity in alls:
        if entity not in entitys:
            entitys.append(entity)

    return entitys

if __name__ == "__main__":
    path = '../data/paser.txt'
    paser = open(path, 'r')
    fp = open('../data/career.txt', 'w')
    for x in paser:
        entitys = get_entitys(x)
        if 'ORGANIZATION' in entitys and 'TITLE' in entitys:
            pass

