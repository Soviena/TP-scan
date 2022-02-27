import scraper

def recent():
    r = scraper.parse_web("https://informatics.labs.telkomuniversity.ac.id/")
    r = r.find('section',id='post')
    r = r.findAll('h2', class_="entry-title")
    for i in range(len(r)):
        print('[{}] '.format(i)+r[i].find('a').text)
    x = int(input("Pilihan : "))
    return(r[x].find('a')['href'])

def matkul():
    r = scraper.parse_web("https://informatics.labs.telkomuniversity.ac.id/")
    r = r.find('li', id='menu-item-3650').find('ul', class_='sub-menu')
    r = r.findAll('a')
    for i in range(len(r)):
        print('[{}] '.format(i)+r[i].text)
    x = int(input("Pilihan : "))
    return(r[x]['href'])

def selectTP(url):
    r = scraper.parse_web(url)
    r = r.find('div', id='content').find('main', id='main')
    r = r.findAll('h2', class_="entry-title")
    for i in range(len(r)):
        print('[{}] '.format(i)+r[i].find('a').text)
    x = int(input("Pilihan : "))
    return(r[x].find('a')['href'])

def tpDetail(url):
    r = scraper.parse_web(url)
    r = r.find('div', class_='entry-content')
    text = r.findAll('p')
    link = r.findAll('div', class_='wp-block-button')
    for i in text:
        print(i.text+'\n')
    for i in link:
        href = i.find('a')
        print(href.text, href['href'])

def menu():
    print("\n\nCek TP")
    print("[0] Baru di upload")
    print("[1] Daftar mata kuliah")
    print("[2] Exit")
    x = int(input("Pilihan : "))
    if x == 0:
        url = recent()
        print()
        tpDetail(url)
    if x == 1:
        url = matkul()
        url = selectTP(url)
        print()
        tpDetail(url)
    if x == 2:
        exit()

while True:  
    menu()