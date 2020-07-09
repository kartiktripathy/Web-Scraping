'''Web Scraping Introduction'''
'''We would be extracting data from a website and saving it into the CSV format'''

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text #connecting to the web and requesting to get the data in form of text

soup = BeautifulSoup(source, 'lxml') #getting the html code from the web

csv_file = open('cms_scrape.csv', 'w') #definging a csv file

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link']) #defing the headers of the csv

for article in soup.find_all('article'): #find all the sections with article
    headline = article.h2.a.text #get the text of the header from the article , not the whole soup
    print(headline)

    summary = article.find('div', class_='entry-content').p.text #in div, with class entry-content find the text in p section of html
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src'] #get the youtube link

        vid_id = vid_src.split('/')[4] #formatting for the link
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link]) #appending the values in the headers of the csv in every iteration

csv_file.close()