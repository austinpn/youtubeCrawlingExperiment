import requests
from bs4 import BeautifulSoup

def fetch_link(url):
    source = requests.get(url).text
    soup= BeautifulSoup(source , 'lxml')
    url_ls=[]
    links = soup.find_all('loc')
    for link in links: 
        url_ls.append(link.text)
    return(url_ls)

followed = fetch_link('https://www.youtube.com/yt/sitemap/sitemap.xml')
full_ls = fetch_link('https://www.youtube.com/yt/sitemap/sitemap.xml')


for x in range(6):        
    temp = []
    for link in followed:
        #print(link)
        temp = temp + fetch_link(link)
    followed = temp
    full_ls = full_ls+temp

with open('crawl.txt' , 'w') as f:
    for link in full_ls:
        f.write(link + '\n')

print(full_ls)
    