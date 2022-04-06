import requests
from bs4 import BeautifulSoup
import csv
import time

with open('results.csv', 'r') as read_obj: # read csv file as a list of lists
  csv_reader = csv.reader(read_obj) # pass the file object to reader() to get the reader object
  list_of_pages = list(csv_reader) # Pass reader object to list() to get a list of lists

for pages in list_of_pages:
    for page in pages:
        
        url = page
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for title in soup.find_all('title'):
            page = dict({page: title.get_text()})
            print(page)
        time.sleep(3)

with open('titles.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(list_of_pages)