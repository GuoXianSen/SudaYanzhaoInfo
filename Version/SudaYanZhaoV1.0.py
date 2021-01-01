import requests
import os
from bs4 import BeautifulSoup

url = "http://yjs.suda.edu.cn/8365/list1.htm"  # 苏大研究生招生网页

news = []  # 存储每一条信息以及信息的日期
# date = []
urls = []  # 存储信息的网页链接

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

contents = soup.find_all('ul', attrs={"class": "title-list title-list-light"})

for new in contents:
    news.append(new.text)
    # print(new.get_text())

print(news[0])
os.system('pause')
# for new in news:
#     print(new)
# print(r.content.decode('utf-8'))
