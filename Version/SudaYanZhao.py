import requests
import os
from bs4 import BeautifulSoup

print("=============================")
print("Author:B站&YouTube：Clay_Guo")
print("=============================")

url = "http://yjs.suda.edu.cn/8365/list1.htm"  # 苏大研究生招生网页

news = []  # 存储每一条信息以及信息的日期
# date = []
urls = []  # 存储信息的网页链接

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

contents = soup.find_all('ul', attrs={"class": "title-list title-list-light"})

lianjie = []

for new in contents:
    news.append(new.text)
    lianjie = new.find_all('a')
    # print(new.get_text())

for url in lianjie:
    urls.append("http://yjs.suda.edu.cn" + url['href'])
    # print("http://yjs.suda.edu.cn/"+ url['href'])

datas = news[0].split('\n\n')[1:-1]

# print(datas)

select = datas[:5]
a = 0
for data in select:
    print(data + urls[a])
    a = a + 1

# print(news)

os.system('pause')

# for new in news:
#     print(new)
# print(r.content.decode('utf-8'))
