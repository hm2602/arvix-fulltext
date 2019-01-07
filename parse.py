import requests
from bs4 import BeautifulSoup
import csv
import time
import os

def read_in_for_scraper(filepath):
    with open('data/'+filepath) as f:
        print(filepath)
        content = f.read()
        content = content.replace("\n","")
        return content


def pull_articles(content, csv_out):
    try:
        print("hi")
        soup = BeautifulSoup(content,'html.parser')
        articles = soup.find_all("td", {'class': 'snipp'})
        for a in articles:
        	print("\n.....\n")
        	titleElem = a.find("span", {'class': "title"})
        	title=titleElem.get_text()
        	print(title)
        	
        	queryWordsElem=titleElem.find_all("b")
        	queryWords = []
        	for q in queryWordsElem:
        		queryWords.append(q.get_text())
        	queryWords = list(set(queryWords))
        	print(queryWords)
        	yearElem = a.find("span", {'class': "year"})
        	year=yearElem.get_text()
        	print(year)

        	arvixIdElem=a.find("a", {'class':"url"})
        	arvixId = arvixIdElem.get_text()
        	print(arvixId)

        	csv_out.writerow([year,arvixId,title,queryWords])

        return subj_text
    except:
        return None

def main():
	out = open('results/result_meta.csv','w')
	csv_out=csv.writer(out,dialect='excel-tab')
	files = os.listdir('data')
	for file in files:
		if (".DS_Store") in file:
			continue
		xml = read_in_for_scraper(file)
		pull_articles(xml, csv_out)


main()