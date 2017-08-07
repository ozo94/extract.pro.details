# coding=utf-8
from bs4 import BeautifulSoup

# 使用beatifulsoup获取内容，会有一大堆的ajax代码，过滤的不够干净(过滤整个网页的时候)
def get_thml_content(s):
    ini_data = []
    soup = BeautifulSoup(s)

    for s in soup.stripped_strings:
        block = str(s.encode('utf-8'))
        content = block.replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '')

        # 一个汉字（包括汉字符号）在unicode中占3个字符，没法用content[-1]的方式来获取结尾符号是什么，需要使用content.endwith()
        ini_data.append(content)

    data = ' '.join(ini_data)
    print data
    return data

if __name__ == '__main__':
    s = file('../../tmp/clean_html.html').read()
    fp = open('../data/selected_mess/test/bs.txt', 'w')
    data = get_thml_content(s)
    fp.write(data)