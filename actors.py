from collections import Counter

def get_actors_unknown(shows_list, show_details):
    unknown_actors = []
    for show_id in show_details:
        for actor_id in show_details[show_id]["cast"]:
            try:
                val = int(show_details[show_id]["cast"][actor_id]["episodes"])
            except ValueError:
                unknown_actors.append(actor_id)
    return set(unknown_actors)

def get_actors(shows_list, show_details, episodes):
    actors = set()
    for show_id in show_details:
        for actor_id in show_details[show_id]["cast"]:
            try:
                if int(show_details[show_id]["cast"][actor_id]["episodes"]) > episodes:
                    actors.add(actor_id)
            except ValueError:
                pass
    return actors

def get_actors(show_id, show_details, episodes):
    actors = []
    for actor_id in show_details[show_id]["cast"]:
        try:
            if int(show_details[show_id]["cast"][actor_id]["episodes"]) > episodes:
                actors.append(actor_id)
        except ValueError:
            pass
    return actors
    
def get_all_actors(shows_list, show_details):
    actors = set()
    for show_id in shows_list:
        for actor_id in show_details[show_id]["cast"].keys():
            actors.add(actor_id)
    return actors