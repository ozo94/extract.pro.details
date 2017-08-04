# 专家主页信息抽取

>在有一系列专家主页url的基础上，爬取主页中所有的内容，完场信息抽取

- 和传统的爬虫爬取不同，各个专家的主页模板差异性很大（没法通过统一的爬虫模板去爬取数据，整理成对应的结构化数据）
- 爬取对应主页所有的文本内容（涉及到标签的去除）
- 信息抽取，涉及到自然语言处理的知识，本文的处理工具主要使用斯坦福大学的coreNLP  
https://stanfordnlp.github.io/CoreNLP/index.html


## 项目结构
![None](http://omouah54e.bkt.clouddn.com/CRWAL_PRO_DETAILS/1.PNG)
### details
是scrpay爬虫部分（具体自行参考scrapy官方文档），爬取专家主页  
**内容存储在根目录的tmp文件**   
contets.txt：逐行存储（一行为一个专家主页的所有内容）  
tags.txt：对应专家的名字，学校，学院  
**依赖**  
- clean_html：  
调用 readability 模块，去除网页的头尾（获得比较干净的body）
- selected_mess:  
将clean_html放入该模块，去除标签，获取主体内容
  

### selected_mess  
>主页内容处理，去除标签,主要有三种方法(beautifulsoup, htmlpaser, re正则匹配)  
 
**数据存放：data/selected_mess**   
主要函数：split_sentence  
将contets中的每行内容进行粗略的断句，并建立映射表 

### extrat_info
>进一步处理sentences，去除英文和标点符号（中，英），放入coreNLP模型工具中跑出实体内容。
建立实体规则，筛选并给出所需条目


