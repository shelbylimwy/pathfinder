# PathFinder (Job Data Webscraper)

## About

PathFinder is a command-line webscrapping program written in python - it takes in job title request, then output Australian job data from the job site Indeed.com as a csv file.

## Libraries

- BeautifulSoup
- requests
- pandas
- sys

## Usage

User will input a **job title** and **preferred name of csv file**. The PathFinder program will output a csv file containing information about active job postings, company names, salaries, location and job description summary related to the job title requested. The program specifically collects data from the Australian job market.

```
python pathfinder.py [job title] [name of csv]

```
## Example

```
python pathfinder.py psychologist psych-career
```

It will return all active job postings data in Australia with the job title 'psychologist' and output the data into a csv file called 'psych-career.csv'.
