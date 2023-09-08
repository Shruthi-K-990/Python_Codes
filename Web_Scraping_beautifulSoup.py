import bs4   #beautiful soup - webscraping
import requests


#############################headers extracted frpm wikepidiea source###############
res = requests.get('https://en.wikipedia.org/wiki/Room_641A')
soup = bs4.BeautifulSoup(res.text,'lxml')
for item in soup.select('.mw-headline'):
    print(item.text)
print()
for x in soup.select('h2'):
    print(x.text)
#################################Image#########################################
res = requests.get('https://en.wikipedia.org/wiki/Hanuman')
soup = bs4.BeautifulSoup(res.text,'lxml')
im = soup.select('.mw-default-size')
print(type(im))
print(im)

c = requests.get('http://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/StandingHanumanCholaDynasty11thCentury.jpg/180px-StandingHanumanCholaDynasty11thCentury.jpg','lxml')
f = open('new_image.jpg','wb')
print(f.write(c.content))
f.close()

