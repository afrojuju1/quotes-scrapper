import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.goodreads.com/quotes')

soup = BeautifulSoup(response.text, 'html.parser')

# with open('quote.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     headers = ['Text']
#     csv_writer.writerow(headers)

#     for quote in quotes:
#         title = 'n/a' # post.find(class_='post-title').get_text().replace('\n', '')
#         # link = post.find('a')['href']
#         # date = post.select('.post-date')[0].get_text()
#         # author = quote.select(class_='authorOrTitle').get_text()
#         text = quote.get_text()
#         text = text.strip(' ')
#         print(text)
#         csv_writer.writerow([text])

# gather tags information
# tags = soup.find_all(class_='greyText smallText left')
# for a in soup.find_all('a', href=True):
#     print "Found the URL:", a['href']
# links = soup.find_all('a', href=True, text=True)
# for link in links:
#   href = link.get('href')
#   # tagText = link.get_text()
#   if '/quotes/tag' in href:
#     tag = link.get_text()
#     print(href)
#     print(tag)

def getTags(quote):
  links = soup.find_all('a', href=True, text=True)
  text = quote.get_text()
  print(text)
  tagList = []
  for link in links:
    href = link.get('href')
    if '/quotes/tag' in href:
      tag = link.get_text()
      tagList.append(tag)
  print(tagList)
  print('\n\n')

quotes = soup.find_all(class_='quoteText')
print(soup)
# for quote in quotes:
#     title = 'n/a' # post.find(class_='post-title').get_text().replace('\n', '')
#     # link = post.find('a')['href']
#     # date = post.select('.post-date')[0].get_text()
#     # author = quote.select(class_='authorOrTitle').get_text()
#     text = quote.get_text()
#     getTags(quote)
#     # text = text.strip(' ')
#     # print(text)

# def say(say_please=False):
#     msg = "Can you buy me a beer?"
#     return msg, say_please