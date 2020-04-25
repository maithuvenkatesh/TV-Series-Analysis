import json 

print "Loading JSON files"
shows_list = json.load(file("./data/shows_list_with_years.json", "r"))
show_details = json.load(file("./data/show_details_1.json", "r"))
show_details.update(json.load(file("./data/show_details_2.json", "r")))

header = "Id,Label,Size\n"
with open("gephi_data/tvn2_nodes.csv", "a") as outfile:
    outfile.write(header)

out = ""
counter = 0
for show_id in shows_list:
    counter += 1
    
    name = shows_list[show_id]["name"]
    year = shows_list[show_id]["year"]
    seasons = show_details[show_id]["seasons"]
    out = "%s,%s %s,%s\n" % (show_id, name, year, seasons)
    print "Writing " + str(counter) + " file" 
    with open("gephi_data/tvn2_nodes.csv", "a") as outfile:
        outfile.write(out.encode("ascii", "ignore"))