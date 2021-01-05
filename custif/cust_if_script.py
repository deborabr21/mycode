#!/usr/bin/env python3

message = "What chicken wing flavor are you?"

while True:
    answer1 = input("Pick a dipping sauce to go with your wings: blue cheese, ranch or none? ").lower()
    answer2 = input("What is your beverage choice: beer, soda or milk? ").lower()

    if answer1 == "blue cheese" and answer2 == "beer":
        print("You are a Parmesan Garlic Wing!")
        break
    elif answer1 == "blue cheese" and answer2 == "soda":
        print("You are a Pinneaple-Teriaky Wing!")
        break
    elif answer1 == "blue cheese" and answer2 == "milk":
        print("You are a Honey Garlic Wing!")
        break		
    elif answer1 == "ranch" and answer2 == "beer":
        print("You are a Honey BBQ Wing!")
        break
    elif answer1 == "ranch" and answer2 == "soda":
        print("You are a Teriaky Wing!")
        break
    elif answer1 == "ranch" and answer2 == "milk":
        print("You are a Jerk Wing!")
        break
    elif answer1 == "none" and answer2 == "beer":
        print("You are a Buffalo Wing!")
        break
    elif answer1 == "none" and answer2 == "soda":
        print("You are a Chocolate-Cherry Wing!")
        break
    elif answer1 == "none" and answer2 == "milk":
        print("You are a Plain Wing!")
        break
    else:
        print("You must provide a valid answer")

			
			
			

