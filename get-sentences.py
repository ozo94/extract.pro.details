# coding=utf-8
from extract_info import split_sentence, choose_data

# path
CONTENTS = 'tmp/contents.txt'
IDS = 'tmp/tags.txt'

SENTENCES = 'data/sentences/sentences.txt'
TAGS = 'data/sentences/tags.txt'
CLEAN_TXT = 'data/sentences/clean_ch.txt'

MIN_LEN = 20
MAX_LEN = 100

# 文本断句
contents = open(CONTENTS, 'r')
ids = open(IDS, 'r')

result = open(SENTENCES, 'w')
tags = open(TAGS, 'w')

split_sentence.get_result(contents, result, tags, ids, MIN_LEN, MAX_LEN)

# 去除句子中的标点和符号
datas = open(SENTENCES, 'r')
clean_ch = open(CLEAN_TXT, 'w')

for data in datas:
    data = data.strip('\n')

    data = choose_data.remove_qoutes(data)
    data = choose_data.remove_en(data)

    data = ' '.join(data.split()).strip(' ')
    if data == '':
        data = '0'
    # print data
    clean_ch.write(data + '\n')
