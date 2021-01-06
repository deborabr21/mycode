#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for dict in farms: #looping across every dictionary in the list (farms)
    # add something to check if the value of "name" is equal to "NE Farm"
    if dict["name"] == "NE Farm":
        print (dict["agriculture"])
