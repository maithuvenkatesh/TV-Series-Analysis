import json 

def add_edge(id_a, id_b, show_details):
    actors_a = show_details[id_a]["cast"].keys()
    actors_b = show_details[id_b]["cast"].keys()

    # Get all actors in both
    actors = set(actors_a) & set(actors_b)
    weight = int(len(actors))

    if weight > 1:
        edge = "%s,%s,%s,%s\n" % (id_a, id_b, "Undirected", weight)
        with open("gephi_data/tvn1_edges.csv", "a") as outfile:
            outfile.write(edge.encode("ascii", "ignore"))

print "Loading JSON files"
shows_list = json.load(file("./data/shows_list_with_years.json", "r"))
show_details = json.load(file("./data/show_details_1.json", "r"))
show_details.update(json.load(file("./data/show_details_2.json", "r")))

header = "source,target,type,weight\n"
with open("gephi_data/tvn1_edges.csv", "a") as outfile:
    outfile.write(header)

out = ""
seen_shows = set()
counter = 0
for id_a in shows_list:
    counter += 1
    print "Processing show number " + str(counter)
    for id_b in shows_list:
        if id_a == id_b:
            break
        if id_a+id_b in seen_shows:
            break
        seen_shows.add(id_a+id_b)
        add_edge(id_a, id_b, show_details)
    