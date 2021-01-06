#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

answer = input("Please choose a farm: NE Farm, W Farm or SE Farm: ")
for dict in farms:
    if answer == dict["name"]:
        print(dict["agriculture"])
