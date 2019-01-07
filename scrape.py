from selenium import webdriver
import re

driver = webdriver.Chrome()
for x in range(200,380,10):
	driver.get('http://search.arxiv.org:8081/?query=health+OR+medicine+OR+medical+OR+doctor+OR+wellness+OR+illness+OR+disease+OR+clinical&in=cs&startat='+str(x))
	fileName = int(x/10)+1
	with open('data/page'+str(fileName)+'.html','w') as f:
		source = driver.page_source
		source = re.split(r'<html',source,maxsplit=1)[1]
		f.write("<html"+source)
driver.quit()