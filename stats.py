import json
import actors

print "Loading JSON files"
shows_list = json.load(file("./data/shows_list_with_years.json", "r"))
show_details = json.load(file("./data/show_details_1.json", "r"))
show_details.update(json.load(file("./data/show_details_2.json", "r")))
actors_in_unknown_episodes = actors.get_actors_unknown(shows_list, show_details)
all_actors = actors.get_all_actors(shows_list, show_details)
actors_in_more_than_one_episode = actors.get_actors(shows_list, show_details, 1)
actors_in_more_than_two_episodes = actors.get_actors(shows_list, show_details, 2)
actors_in_more_than_three_episodes = actors.get_actors(shows_list, show_details, 3)
actors_in_more_than_four_episodes = actors.get_actors(shows_list, show_details, 4)

print "Number of distinct shows: " + str(len(shows_list))
print "shows_list == show_details: " + str(len(shows_list) == len(show_details))
print "Total number of distinct actors: " + str(len(all_actors))
print "Number of actors in unknown episodes: " + str(len(actors_in_unknown_episodes))
print "Number of actors who appeared in more than one episode in any TV show: " + str(len(actors_in_more_than_one_episode)) 
print "Number of actors who appeared in more than two episodes in any TV show: " + str(len(actors_in_more_than_two_episodes)) 
print "Number of actors who appeared in more than three episodes in any TV show: " + str(len(actors_in_more_than_three_episodes)) 
print "Number of actors who appeared in more than four episodes in any TV show: " + str(len(actors_in_more_than_four_episodes)) 

