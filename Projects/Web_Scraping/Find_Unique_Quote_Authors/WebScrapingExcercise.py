import bs4
import requests

unique_authors = set()
base_url = "https://quotes.toscrape.com/page/{}/"
res = requests.get(base_url.format("1"))
soup = bs4.BeautifulSoup(res.text, 'lxml')
page = 1

#While no more pages get the correct url 
while 'No quotes found!' not in str(soup.select('.col-md-8')[1]):
    res = requests.get(base_url.format(page))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    #Get the authors from every page in a list
    authors = soup.select('small')
    #Iterate through the list of authors and add
    for author in authors:
        unique_authors.add(author.text)
    #Next Page
    page += 1

print(unique_authors)