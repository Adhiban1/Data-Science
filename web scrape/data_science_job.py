import colorama
from colorama import Fore
colorama.init(autoreset=True)

print(f'{Fore.RED}Importing files...')

import re
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from rich.progress import track

print(f'{Fore.BLUE}Chrome Driver...')

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
url = 'https://www.naukri.com/jobs-in-india?clusters=functionalAreaGid&functionAreaIdGid=3&experience=0&cityTypeGid=97&cityTypeGid=183&ctcFilter=6to10&ugTypeGid=12&ugTypeGid=9502'
driver.get(url)

print(f'{Fore.GREEN}Enter pages > ', end='')
n = int(input())

sheet = []

for k in track(range(1, n+1)):
    if k == 1:
        url = 'https://www.naukri.com/jobs-in-india?clusters=functionalAreaGid&functionAreaIdGid=3&experience=0&cityTypeGid=97&cityTypeGid=183&ctcFilter=6to10&ugTypeGid=12&ugTypeGid=9502'
    else:
        url = f'https://www.naukri.com/jobs-in-india-{k}?clusters=functionalAreaGid&functionAreaIdGid=3&experience=0&cityTypeGid=97&cityTypeGid=183&ctcFilter=6to10&ugTypeGid=12&ugTypeGid=9502'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    article = soup.find_all('article', class_='jobTuple bgWhite br4 mb-8')
    for i in article:
        job = i.div.div.a.text
        company = i.div.div.div.a.text
        salary = i.div.div.ul.find('li', class_='fleft grey-text br2 placeHolderLi salary').span.text
        link = i.div.div.a['href']
        if 'Not disclosed' not in salary:
            sheet.append([job, company, salary, link])
#             print(job, 
#                   company,
#                   salary, 
#                   link, sep=' : ')
print(f'{Fore.YELLOW}Web Scrape completed')
driver.quit()
print(f'{Fore.CYAN}Working on DataFrame...')
df = pd.DataFrame(sheet, columns=['job', 'company', 'salary', 'link'])
df['min_salary'] = df.salary.apply(lambda x : int(re.findall('\d+', x.replace(',', ''))[0]))
df['max_salary'] = df.salary.apply(lambda x : int(re.findall('\d+', x.replace(',', ''))[1]))
df = df.sort_values('min_salary', ascending=False)
df = df.drop('salary', axis=1)
df = df.drop_duplicates()
print(f'{Fore.RED}DataFrame: {Fore.CYAN}')
print(df[['job', 'company', 'min_salary', 'max_salary']])
print(f'{Fore.GREEN}\nLinks: ')
for i in df.link:
    print(f'{Fore.BLUE}{i}', end=',\n')