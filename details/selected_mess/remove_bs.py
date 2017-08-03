# coding=utf-8
from bs4 import BeautifulSoup

# 使用beatifulsoup获取内容，会有一大堆的ajax代码，过滤的不够干净(过滤整个网页的时候)
def get_thml_content(s):
    ini_data = []
    soup = BeautifulSoup(s)

    symbol = [',', '，', '、', '-', '——', '《', '(', '（', ':', '：', '。', ']', '}', '】', ':', '：']


    for s in soup.stripped_strings:
        block = str(s.encode('utf-8'))
        x = block.replace('\t', '').replace('\n', '').replace('\r', '')

        flag = 0
        for end in symbol:
            if x.endswith(end):
                # 一个汉字（包括汉字符号）在unicode中占3个字符，没法用x[-1]的方式来获取结尾符号是什么
                flag = 1
                break

        if flag:
            ini_data.append(x)
        else:
            ini_data.append(x + '。')

    data = ''.join(ini_data)
    print data
    return data

if __name__ == '__main__':
    s = file('../../tmp/clean_html.html').read()
    fp = open('../test/result_bs.txt', 'w')
    data = get_thml_content(s)
    fp.write(data)