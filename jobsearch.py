import requests
from bs4 import BeautifulSoup
import csv

# Create the csv file for the data to be exported to
file = open('jobslist.csv', 'w', newline='')
writer = csv.writer(file)

# Add rows to the file
writer.writerow(['Job Title', 'Job Link'])

# Define the functions for each job website
def totalJobs():
    website = requests.get("https://www.totaljobs.com/jobs/junior-developer/in-nr31-0lt?radius=30&postedwithin=3").text
    soup = BeautifulSoup(website, 'lxml')
    for jobdiv in soup.find_all('div', class_='job-title'):
        title = jobdiv.h2.text
        link = jobdiv.find('a')['href']
        writer.writerow([title, link])

def indeedJobs():
    website = requests.get("https://www.indeed.co.uk/jobs?as_and=junior+developer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=25&l=Great+Yarmouth&fromage=3&limit=20&sort=date&psf=advsrch").text
    soup = BeautifulSoup(website, 'lxml')
    for jobdiv in soup.find_all('div', class_='title'):
        title = jobdiv.a.text
        link = jobdiv.find('a')['href']
        writer.writerow([title, "https://www.indeed.co.uk/" + link])

def reedJobs():
    website = requests.get("https://www.reed.co.uk/jobs/junior-developer-jobs-in-nr310lt?datecreatedoffset=LastThreeDays&proximity=30").text
    soup = BeautifulSoup(website, 'lxml')
    for jobs in soup.find_all('article', class_='job-result'):
        title = jobs.h3.text
        link = jobs.find('a')['href']
        writer.writerow([title, 'https://www.reed.co.uk/' + link])

totalJobs()
indeedJobs()
reedJobs()

file.close()
