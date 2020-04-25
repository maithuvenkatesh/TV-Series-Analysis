# Scrapes cast and seasons information for TV shows

import json
import urllib2
import re
from bs4 import BeautifulSoup

counter = 0

print "Loading JSON"
shows = json.load(file("./data/shows_list.json", "r"))

show_details = json.load(file("./data/show_details.json", "r"))
show_details.update(json.load(file("./data/show_details_2.json", "r")))

base_url1 = "http://www.imdb.com/title/"
base_url2 = "/fullcredits?ref_=tt_ov_st_sm"
out = {}
for show_id in shows:
    counter += 1

    if show_id in show_details:
        print str(counter) + "." + "Already written to file" 
    else:
        show = shows[show_id]
        out[show_id] = show

        try:
            print "Processing " + str(out[show_id]["name"])
        except UnicodeEncodeError:
            print "Cannot print the name of this show"

        base_url = base_url1 + show_id + base_url2
        cast_page = BeautifulSoup(urllib2.urlopen(base_url))
        cast = {}
        for entry in cast_page.find("table", {"class": "cast_list"}).find_all("tr")[1:]:
            if entry.find("td", {"class": "castlist_label"}):
                break
            else: 
                actor_id = entry.find("td", {"class": "itemprop"}).find("a")["href"].split("/")[2]
                cast[actor_id] = {}
                cast[actor_id]["actor_name"] = entry.find("td", {"class": "itemprop"}).find("a").find("span", {"class": "itemprop"}).string
                episodes = entry.find("td", {"class": "character"}).find("div").text

                if not len(re.findall("\d+ episode", episodes)) == 0:
                    cast[actor_id]["episodes"] = re.findall("\d+ episode", episodes)[0].split(" ")[0]
                else: 
                    cast[actor_id]["episodes"] = "Unknown"
        
        out[show_id]["cast"] = cast

        show_page = BeautifulSoup(urllib2.urlopen(show["imdb_url"]))
        if "TV Series" in show_page.find("div", {"class": "infobar"}).text:
            try: 
                seasons = len(show_page.find("div", {"class": "seasons-and-year-nav"}).find_all("div")[2].find_all("a"))
            except AttributeError:
                seasons = 0
        else:
            seasons = "TV Movie"

        out[show_id]["seasons"] = seasons

        with open("./data/show_details_2.json", "w") as outfile:
            json.dump(out, outfile)

        try:
            print str(counter) + "." + str(out[show_id]["name"]) + " written to file"
        except UnicodeEncodeError:
            print str(counter) + "." + "written to file" 