import os
import argparse
from bs4 import BeautifulSoup
import re
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--directory', type=str, required=True)
args = parser.parse_args()

path = args.directory

dir_list = os.listdir(path)

header_list = [
               'Page Name', 'Errors', 'Principle1', 'Principle2','Principle3', 
               'Principle4', '1_1_1', '1_2_1', '1_2_2', '1_2_3', '1_2_4', 
               '1_2_5', '1_2_6', '1_2_7', '1_2_8', '1_2_9', '1_3_1', 
               '1_3_2', '1_3_3', '1_3_4', '1_3_5', '1_3_6', '1_4_1', 
               '1_4_2', '1_4_3', '1_4_4', '1_4_5', '1_4_6', '1_4_7', 
               '1_4_8', '1_4_9', '1_4_10', '1_4_11', '1_4_12', '1_4_13', 
               '2_1_1', '2_1_2', '2_1_3', '2_1_4', '2_2_1', '2_2_2', 
               '2_2_3', '2_2_4', '2_2_5', '2_2_6', '2_3_1', '2_3_2', 
               '2_3_3', '2_4_1', '2_4_2', '2_4_3', '2_4_4', '2_4_5',
               '2_4_6', '2_4_7', '2_4_8', '2_4_9', '2_4_10', '2_5_1',
               '2_5_2', '2_5_3', '2_5_4', '2_5_5', '2_5_6', '3_1_1', 
               '3_1_2', '3_1_3', '3_1_4', '3_1_5', '3_1_6', '3_2_1',
               '3_2_2', '3_2_3', '3_2_4', '3_2_5', '3_3_1', '3_3_2',
               '3_3_3', '3_3_4', '3_3_5', '3_3_6', '4_1_1', '4_1_2', '4_1_3',]

with open('a11y.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header_list)
    writer.writeheader()
 
for item in dir_list:
    if item.endswith('html'):
        if item != "index.html":
            soup = BeautifulSoup(open(item, encoding="utf8"), "html.parser")
            page_name = soup.find('h1').find('a').get('href')
            
            errors = soup.find_all("li", {"data-result-level" : "error"})
            num_errors = len(errors)
            print(page_name + " " + str(num_errors))
            
            page_info = {'Page Name':page_name, 'Errors':num_errors}
            principles = {'Principle1':0, 
                          'Principle2':0, 
                          'Principle3':0, 
                          'Principle4':0}
            standards = {'1_1_1':0, '1_2_1':0, '1_2_2':0, '1_2_3':0,
                         '1_2_4':0, '1_2_5':0, '1_2_6':0, '1_2_7':0,
                         '1_2_8':0, '1_2_9':0, '1_3_1':0, '1_3_2':0,
                         '1_3_3':0, '1_3_4':0, '1_3_5':0, '1_3_6':0,
                         '1_4_1':0, '1_4_2':0, '1_4_3':0, '1_4_4':0,
                         '1_4_5':0, '1_4_6':0, '1_4_7':0, '1_4_8':0,
                         '1_4_9':0, '1_4_10':0, '1_4_11':0, '1_4_12':0,
                         '1_4_13':0, '2_1_1':0, '2_1_2':0, '2_1_3':0,
                         '2_1_4':0, '2_2_1':0, '2_2_2':0, '2_2_3':0,
                         '2_2_4':0, '2_2_5':0, '2_2_6':0, '2_3_1':0,
                         '2_3_2':0, '2_3_3':0, '2_4_1':0, '2_4_2':0,
                         '2_4_3':0, '2_4_4':0, '2_4_5':0, '2_4_6':0,
                         '2_4_7':0, '2_4_8':0, '2_4_9':0, '2_4_10':0,
                         '2_5_1':0, '2_5_2':0, '2_5_3':0, '2_5_4':0,
                         '2_5_5':0, '2_5_6':0, '3_1_1':0, '3_1_2':0,
                         '3_1_3':0, '3_1_4':0, '3_1_5':0, '3_1_6':0,
                         '3_2_1':0, '3_2_2':0, '3_2_3':0, '3_2_4':0,
                         '3_2_5':0, '3_3_1':0, '3_3_2':0, '3_3_3':0,
                         '3_3_4':0, '3_3_5':0, '3_3_6':0, '4_1_1':0,
                         '4_1_2':0, '4_1_3':0,}
            
            for err in errors:
                text = err.find('code').get_text()
                match_principles = re.search(r'Principle[0-9]', text)
                if match_principles: 
                    principles[match_principles.group(0)] += 1
                match_standards = re.search(r'[0-9]_[0-9]_[0-9]+', text)
                if match_standards:
                    standards[match_standards.group(0)] += 1
                        
            csv_dict = {**page_info, **principles, **standards}
            
            with open('a11y.csv', 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=csv_dict.keys())
                writer.writerow(csv_dict)            