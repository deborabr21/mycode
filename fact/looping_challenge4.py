#!/usr/bin/env python3
  
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

forbidden= ["carrots","celery"] # list of things we want to exclude

print("""
Choose one of the following:
0. NE Farm
1: W Farm
2. SE Farm
""")
answer = int(input(">"))
for x in farms[answer]["agriculture"]:
    if x not in forbidden:
        print(x)
