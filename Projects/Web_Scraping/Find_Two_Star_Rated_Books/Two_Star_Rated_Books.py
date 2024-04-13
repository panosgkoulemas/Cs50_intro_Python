#GOAL : Get the title of every book with a 2-star rating 
#from https://books.toscrape.com/index.html¶

import requests
import bs4

count = 0
two_star_book = []
for i in range(1,51):
    print(f'Page {i}')
    res = requests.get(f'https://books.toscrape.com/catalogue/page-{i}.html')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    count = 0
    for book in soup.select('h3 a'):
        if soup.select("p.star-rating")[count]['class'][1] == "Two":
            print(book['title'])
            two_star_book.append(book['title'])
        count += 1
    print("\n")