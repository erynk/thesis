import argparse
from googlesearch import search

 
# create parser
parser = argparse.ArgumentParser(description="This program makes a domain restricted Google search and returns the first ten results")
 
# add arguments to the parser
parser.add_argument("site", nargs='?', type=str, default="www.mines.edu", help="Enter the web address of the website to be queried.")
 
# parse the arguments
args = parser.parse_args()
 
# get the arguments value and join it to the domain specific search string
query = "site: " + args.site

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
 
for j in search(query, tld="com", num=10, stop=10, pause=2):
    print(j)