# Scrapes all the year information for 
# TV shows in the IMDB list obtained by scraper.py

import urllib2
import json
import re
from bs4 import BeautifulSoup

print "Loading JSON files"
shows_list = json.load(file("./data/shows_list.json", "r"))
updated_shows_list = json.load(file("./data/shows_list_with_years.json", "r"))

print "Getting show details"
counter = 0
for show_id in shows_list:
    counter += 1
    show = shows_list[show_id]

    if show_id in updated_shows_list:
        print str(counter) + "." + "Already written to file"
    else:
        updated_shows_list[show_id] = show
        show_page = BeautifulSoup(urllib2.urlopen(shows_list[show_id]["imdb_url"]))
        year = show_page.find("span", {"class": "nobr"}).text
        updated_shows_list[show_id]["year"] = year.replace(u'\u2013', "-")

        print "Writing " + str(counter) + " to JSON file"
        with open("./data/shows_list_with_years.json", "w") as outfile:
            json.dump(updated_shows_list, outfile)