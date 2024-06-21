import requests
response=requests.get("https://www.naukri.com/skilllabs-overview-3442166?tab=jobs&searchId=17112769340583111&src=orgCompanyListing")
from bs4 import BeautifulSoup

print(response.text)

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
