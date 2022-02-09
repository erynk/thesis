from googlesearch import search
import csv
import time

sites = []

with open('sites.txt') as file:
    for line in file:
        sites.append(line.rstrip())



# to search

'''
Required Function and its parameters 

query: query string that we want to search for.
TLD: TLD stands for the top-level domain which means we want to search our results on google.com or google. in or some other domain.
lang: lang stands for language.
num: Number of results we want.
start: The first result to retrieve.
stop: The last result to retrieve. Use None to keep searching forever.
pause: Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapses will make your program slow but it’s a safe and better option.
Return: Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
'''

for site in sites:
    query = "site:" + site
    results = []
    for j in search(query, tld="com", num=10, stop=10, pause=2):
        results.append(j)
        print(j)
    with open('results.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(results)
    time.sleep(3)
           