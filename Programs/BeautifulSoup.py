
#Beautiful Soup Code

import requests  
from bs4 import BeautifulSoup
import re
#https://en.wikipedia.org/
url = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'
response = requests.get(url)
print(response.text)
print(response.content)
# r.text is the content of the response in Unicode, and r.content is the content of the response in bytes.

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
print(html_soup)

award_list=html_soup.find_all("tr",{"style":'background:#FAEB86'})
print(len(award_list))

first_award=award_list[0]
print("*"*80)
print(first_award)

val=first_award.find("a",{"href":re.compile("film\)")}).get("href")
print(val)
#other way to retrieve href data


print(val)
data=first_award.find("a",{"href":re.compile("film\)")})
print(data.text)
val=data["href"]


#https://en.wikipedia.org/wiki/Wings_(1927_film)
newurl="https://en.wikipedia.org"+val
print(newurl)
newresponse = requests.get(newurl)
print(newresponse.text)
newdata=BeautifulSoup(newresponse.text,"html.parser")

title=newdata.select("h1[id='firstHeading'] i")[0].text
title1=newdata.select_one("h1[id='firstHeading'] i").text
print(title)
print(title1)

title=newdata.select("tr:-soup-contains('Directed by') a[href*='/wiki/']")[0].text
title1=newdata.select_one("tr:-soup-contains('Directed by') a[href*='/wiki/']").text
print(title)
print(title1)

title=newdata.select("tr:contains('Release dates') li")[0].text
title1=newdata.select_one("tr:contains('Release dates') li").text
print(title)
print(title1)

data['title']=response.css(r"h1[id='firstHeading'] i::text").extract()
data['directedby']=response.css(r"::text").extract()
#data['starring']=-----
data['releasedate']=response.css(r"::text").extract()

#response.css can be replaced by 

names=[]
directedby=[]
releaseddate=[]
for movie in award_list:
    data=movie.find("a",{"href":re.compile("film\)")})
    if data!=None:
        val=data["href"]
        newurl="https://en.wikipedia.org"+val
        print(newurl)
        newresponse = requests.get(newurl)
        newdata=BeautifulSoup(newresponse.text,"html.parser")
        title=newdata.select_one("h1[id='firstHeading'] i")
        if title!=None:
            names.append(title.text)
        else:
            names.append("")
        director=newdata.select("tr:-soup-contains('Directed by') a[href*='/wiki/']")[0].text
        directedby.append(director)
        releasedt=newdata.select_one("tr:contains('Release dates') li")
        if releasedt!=None:
            releaseddate.append(releasedt.text)
        else:
            releaseddate.append("")
d={"title":names,"directedby":directedby,"releaseddate":releaseddate}
import pandas as pd
df=pd.DataFrame(d)
print(df.head())