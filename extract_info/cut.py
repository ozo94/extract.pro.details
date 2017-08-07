# coding=utf-8
import jieba

str = '获上海市科技进步一等奖1次、二等奖2次，教育部科技进步一等奖1次'
result = jieba.cut(str)
print ' '.join(result)


# print len('现为同济大学控制科学与工程系教授、博士生导师，电子与信息工程学院院长')
print '测试结果 \r  2'

token = '奖'

if token in str:
    print token