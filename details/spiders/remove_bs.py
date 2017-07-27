from bs4 import BeautifulSoup

def get_thml_content(s):
    ini_data = []
    data = ''
    soup = BeautifulSoup(s)

    for s in soup.stripped_strings:
        block = str(s.encode('utf-8'))
        x = block.replace('\t', '').replace(' ', '').replace('\n', '').replace('\r', '')
        if x:
            ini_data.append(x)

    data = ''.join(ini_data)
    print '\n',data
    return data

if __name__ == '__main__':
    s = file('../../test.html').read()
    fp = open('result_bs.txt', 'w')
    data = get_thml_content(s)
    fp.write(data)