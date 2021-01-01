import requests
import os
from bs4 import BeautifulSoup

from src.mail2me import mail

url = "http://yjs.suda.edu.cn/8365/list1.htm"  # 苏大研究生招生网页

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.105 Safari/537.36 "

}

news = []  # 存储每一条信息以及信息的日期
urls = []  # 存储信息的网页链接

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

contents = soup.find_all('ul', attrs={"class": "title-list title-list-light"})

# print(contents)

lianjie = []

for new in contents:
    news.append(new.text)
    lianjie = new.find_all('a')

for url in lianjie:
    urls.append("http://yjs.suda.edu.cn" + url['href'])
    # print("http://yjs.suda.edu.cn/"+ url['href'])

# print(urls[0])
# print(new.get_text())
# print("http://yjs.suda.edu.cn/"+new.a['href'])


# urls = soup.find_all()

datas = news[0].split('\n\n')[1:-1]

# print(datas)

select = datas[:5]

ret = mail(select[0] + urls[0] + select[1] + urls[1] + select[2] + urls[2] + select[3] + urls[3] + select[4] + urls[4])
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
# for data in select:
#     print(data)

# print(news)

# os.system('pause')

# for new in news:
#     print(new)
# print(r.content.decode('utf-8'))
