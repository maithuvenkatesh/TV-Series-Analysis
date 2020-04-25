# Scrapes all the TV shows in the IMDB list

import urllib2
import json
from bs4 import BeautifulSoup

base_url1 = "http://www.imdb.com/search/title?num_votes=5000,&sort=moviemeter&start="
base_url2 = "&title_type=tv_series"
counter = 1
shows = {}

print "Getting TV shows"
while len(shows) < 859:
    base_url = base_url1 + str(counter)+ base_url2
    shows_page = BeautifulSoup(urllib2.urlopen(base_url), "html.parser")

    print shows_page.findAll("div", {"class":"lister-item"})
"""
    for entry in shows_page.find("lister-list", {"class":"lister-item"}).find_all("tr")[1:]:
        name = entry.find("td", {"class":"title"}).find("a").string

        imdb_url =  "http://www.imdb.com" + entry.find("td", {"class":"title"}).find("a").get("href")
        imdb_id = imdb_url.split("/")[4]
        shows[imdb_id] = {"name":name, "imdb_url":imdb_url}
    counter += 50

print "Writing to JSON file"
with open("./data/shows_list.json", "w") as outfile:
    json.dump(shows, outfile)
"""