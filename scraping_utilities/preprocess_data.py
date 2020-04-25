# This script removes all TV movies from the dataset
# and writes the data back to files
import json

print "Loading JSON files"
show_list = json.load(file("./data/original/shows_list.json", "r"))
show_details = json.load(file("./data/original/show_details_2.json", "r"))

print "Removing TV Movies"
for show_id in show_details:
    try:
        if show_details[show_id]["seasons"] == "TV Movie":
            del show_details[show_id]
            del show_list[show_id]
            break
    except RuntimeError:
        print "Error caught"

print "Writing data"
with open("./data/processed/show_list.json", "w") as outfile:
    json.dump(show_list, outfile)

with open("./data/processed/show_details_2.json", "w") as outfile:
    json.dump(show_details, outfile)