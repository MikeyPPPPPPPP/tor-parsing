#NEED TO HAVE TOR OPEN TO WORK



from bs4 import BeautifulSoup
import requests
sites = []


url = 'http://33cb5x4tdiab2jhe.onion/cat/1'


session = requests.session()

session.proxies = {}

session.proxies['http'] = 'socks5h://127.0.0.1:9150'
session.proxies['https'] = 'socks5h://127.0.0.1:9150'


r = session.get(url)



data = r.text


soup = BeautifulSoup(data, 'lxml')
doc = open('allsites.txt','+w')

for link in soup.find_all('a'):
    sites.append(link.get('href'))
    
for x in sites:
    if 'http://' in x:
        doc.write(x)
        doc.write('\n')
        print(x)
    else:
        pass
doc.close()
