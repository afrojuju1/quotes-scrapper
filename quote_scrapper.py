import requests
from bs4 import BeautifulSoup
from app import db, Quote, Tag

response = requests.get('https://www.goodreads.com/quotes')

soup = BeautifulSoup(response.text, 'html.parser')

def get_tags(quote):
  links = soup.find_all('a', href=True, text=True)
  tags = []
  for link in links:
    href = link.get('href')
    if '/quotes/tag' in href:
      tag = link.get_text()
      tags.append(tag.strip())
  return tags

def scrap_quotes():
  # todo: add logic to treverse all pages. 1 - 100
  # https://www.goodreads.com/quotes?page=1
  quotes = soup.find_all(class_='quoteText')
  # remove all script tags
  [x.extract() for x in soup.find_all('script')]
#   [x.extract() for x in soup.find_all('br')]
  for quote in quotes:
    # del quote['script']
    text = quote.get_text()
    author = quote.find(class_='authorOrTitle').get_text().replace(',', '')
    tags = get_tags(quote)

    save_quote(text, author, tags)
    # print(text)
    # print(author)
    # print('\n\n')

def save_quote(text, author, quoteTags):
  #saves the quote to db
  quote = Quote(text, author)
  db.session.add(quote)
  db.session.flush()

  for qTag in quoteTags:
    tag = Tag(qTag, quote.id)
    db.session.add(tag)
  # commit all the information
  db.session.commit()

# run the function
# scrap_quotes()
