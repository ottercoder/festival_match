import requests
from lxml import html


def get_artists(path, year):
    page = requests.get(path + '/' + str(year))
    tree = html.fromstring(page.content)
    list = tree.xpath(
        '//div["lineup-with-stage"]/div["stage-wrapper"]/div["stage"]/ul["lineup"]/li["artist"]/span["name-time"]/span[@itemprop="name"]//text()')
    return list


def get_festivals_from_file():
    with open("festivals.txt") as file:
        lines = [line.strip() for line in file]
    return lines


def get_festivals():
    path = 'https://www.festicket.com/festivals/?page='
    list = []
    for p in range(1, 37):
        print p
        page = requests.get(path + str(p))
        tree = html.fromstring(page.content)
        for elt in tree.xpath('//div["festival-info"]/h3["festival-title"]//a'):
            url = elt.attrib['href']
            url = trim_url(url)
            list.append(url)
    thefile = open('festivals.txt', 'w')
    for item in list:
        thefile.write("%s\n" % item)
    return list
