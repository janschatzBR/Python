import requests   #executar antes: "pip install requests" ou "py -m pip install -U requests"
from bs4 import BeautifulSoup       #pip install beautifulsoup4
import json

#res = requests.get("https://projetos.digitalinnovation.one/blog")
#res = requests.get("https://digitalinnovation.one/")
res = requests.get("https://www.theguardian.com/international")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

print(res)
#print(res.text)   #traz código-fonte da página
#print(soup)        #traz código-fonte da página com parsing

posts = soup.find_all(class_ = "post")

all_post = []
for post in posts:
    info = post.find(class_ = "post-content")
    title = info.h2.text
    preview = info.p.text
    author = info.find(class_ = "post-author").text
    time = info.find(class_ = "post-date")['datetime']
    all_post.append({
        'title': title,
        'preview': preview,
        'author': author,
        'time': time
    })

    print(all_post)
    with open('posts.json', 'w') as json_file:
        json.dump(all_post, json_file, indent = 3, ensure_ascii = False)