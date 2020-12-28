from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys

# check command line argument
if len(sys.argv) != 3:
    print("Usage: python pathfinder.py [job title] [csv file name] ")
    sys.exit(1)

# extract url from internet
def extract(page, job_title):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    url = f'https://au.indeed.com/{job_title}-jobs-in-Australia?start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# transform into dictionary with important features
def transform(soup):
    divs = soup.findAll('div', class_ ='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_ ='company').text.strip()
        try:
            location = item.find('span', class_ = 'location').text.strip()
        except:
            location = ''

        try:
            salary = item.find('span', class_ ='salaryText').text.strip()
        except:
            salary = ''

        summary = item.find('div', {'class': 'summary'}).text.strip().replace('\n', ' ')

        job = {
            'Title': title,
            'Company': company,
            'Salary': salary,
            'Location': location,
            'Summary': summary
        }

        joblist.append(job)

    return

# create job list
joblist = []

# see what job the user requested
job_requested = sys.argv[1]

# see what the user wants to name csv file as
file_name = sys.argv[2]

# print all jobs in first 5 pages
for i in range(0, 50, 10):
    c = extract(i, job_requested)
    transform(c)

# use dataframe to transform data into csv file
df = pd.DataFrame(joblist)
df.to_csv(f'{file_name}.csv')
