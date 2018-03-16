import requests
from BeautifulSoup import BeautifulSoup
import subprocess

query = 'http://dl.my-film.in/serial/The%20Wire/Season%201%20-%201080p%20BluRay/'


def get_link():
    html = requests.get(query).text
    data = BeautifulSoup(html)
    # print data
    links = []
    for i in data.findAll('a'):
        hlink = i.get('href')
        link = query + hlink
        links.append(link)
    # print links
    extract_links(links)


def extract_links(links):
    for i in links:
        if '1080p' in i:
            print i
            link = i
            download_links(link)
        # elif '720p' in i:
        #     print i
        #     link = i
        #     download_links(link)


def download_links(link):
    commands = ['aria2c', '-x 16', '-s 16', link]
    subprocess.call(commands)


if __name__ == '__main__':
    get_link()
