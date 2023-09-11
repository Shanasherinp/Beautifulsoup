import requests
from bs4 import BeautifulSoup
import re
url = "https://www.technopark.org/job-search"
keywords = ["python"]
output_file = open("jobs.txt","w")
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
jobs = soup.find_all("tr",{"class":"companyList"})
for job in jobs:
    title_element = job.find("a")
    title = title_element.text
    link = title_element["href"]
    company_name = job.find("td",{"class":""})
    company = company_name.find("a").text
    last_date = job.find("td",{"class":""}).date
    #print(title, link)
    #print(last_date)
    date_elements = job.find_all('td', class_='')

    # Regular expression pattern to match a date in the format "dd/mm/yyyy"
    date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')

    # Extract and print valid dates from all matching elements
    for date_element in date_elements:
        date = date_element.text.strip()  # Remove leading/trailing whitespace
        if date_pattern.match(date):
            #print(title, company, date)
            if any(word.lower() in title.lower() for word in keywords):
                print(title,company,date)
                output_file.write(title + " " +  company + " " +  date +"\n" + link + "\n\n")