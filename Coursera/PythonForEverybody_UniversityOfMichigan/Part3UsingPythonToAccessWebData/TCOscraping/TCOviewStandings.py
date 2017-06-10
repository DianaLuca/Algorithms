import urllib.request
import csv
from bs4 import BeautifulSoup
import datetime
import schedule
import time


name = 'TCO_contest'


def scrapingJob():
    print('Scraping TCO contest standings ................')
    url = 'https://community.topcoder.com/longcontest/?module=ViewStandings&rd=16903'

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    table_cells = soup.findAll('td', { 'class' : ['statLt', 'statDk']})

    with open("%s(%s).csv"% (name,datetime.datetime.now().strftime("%d-%m-%Y:%H-%M-%S")), 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(('Handle', 'Score', 'Rank', 'Last Submission Time', 'Language', 'Example Tests', 'Submissions'))
        for i in range(0, len(table_cells), 7):
            wr.writerow([cell.text.strip() for cell in table_cells[i:i+7]])

schedule.every(30).seconds.do(scrapingJob)

while 1:
    schedule.run_pending()
    time.sleep(1)