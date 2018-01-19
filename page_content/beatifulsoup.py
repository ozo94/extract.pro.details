# coding=utf-8
from bs4 import BeautifulSoup

def get_html_content(s):
    ini_data = []
    soup = BeautifulSoup(s)

    for s in soup.stripped_strings:
        block = str(s.encode('utf-8'))
        content = block.replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '')

        # 一个汉字（包括汉字符号）在unicode中占3个字符，没法用content[-1]的方式来获取结尾符号是什么，需要使用content.endwith()
        ini_data.append(content)

    data = ' '.join(ini_data)
    return data
