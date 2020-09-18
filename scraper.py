# Code to scrape the results of any student from "http://exam.msrit.edu/"

import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

url = 'http://exam.msrit.edu/index.php'

values = {'usn' : '<USN Goes Here>',   # Enter the usn here
          'option' : 'com_examresult',
          'task' : 'getResult' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    result_page = response.read().decode("utf-8")

soup = BeautifulSoup(result_page, 'html.parser')
sem = soup.find("div", {"class": "uk-card uk-card-body stu-data stu-data2"}).find('p').get_text(strip=True)[-1:]
credits_registered = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec1"}).find('p').get_text(strip=True)
credits_earned = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec2"}).find('p').get_text(strip=True)
sgpa = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec3"}).find('p').get_text(strip=True)
cgpa = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec4"}).find('p').get_text(strip=True)

# subjects with results of the previous sem
res = soup.find("table", {"class", "uk-table uk-table-striped res-table"}).find_all("tr")[1:]
results = []
for item in res:
    r = []
    data = item.find_all('td')
    for x in data:
        r.append(x.get_text(strip=True))
    results.append(r)


print(sem)  #Semester
print(credits_registered)  #Total Credits Registered by the student for the semester
print(credits_earned)  #Total Credits earned by the student for the semester
print(sgpa)  #Semester Grade Point Average 
print(cgpa)  #Cumulative Grade Point Average
print(results)  #Subject-wise results: Subject Code, Subject Name, Credits Earned, Credits for the subject and Grade
