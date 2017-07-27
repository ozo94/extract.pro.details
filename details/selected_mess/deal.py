# coding=utf-8
import nltk
import jieba
import re

str = open('../spiders/result2.txt', 'r')

for s in str:
    setence = re.split('，|。', s)

for x in setence:
    words = jieba.cut(x ,cut_all=False)
    print ' '.join(words)