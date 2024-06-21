# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:18:58 2024

@author: Administrator
"""

import requests
response=requests.get("https://www.naukri.com/skilllabs-overview-3442166?tab=jobs&searchId=17112769340583111&src=orgCompanyListing")
from bs4 import BeautifulSoup

print(response.content)

#find following values and store it in dataframe using beautifulsoup
#using same link write code for scrapy
#job title, company name, experience rquired, salary, location

#Beautiful Soup Code

html_soup = BeautifulSoup(response.text, 'html.parser')

jobTitle_list=html_soup.find_all("a", class_="title fw700 ellipsis")
print(len(jobTitle_list))
lst = []
for tag in html_soup.find_all("div", class_="info dpflexcol"):
    print(tag.text)
    lst.append(tag)
print(len(lst))

# print(response.text)
# data=BeautifulSoup(response.content,"html.parser")

# # job_title=data.select("a[class='title fw700 ellipsis'] i")[0].text
# job_title2=data.select_one("a[class='title fw700 ellipsis']").content
# # print(job_title)
# print(job_title2)


#Scrapy Code
