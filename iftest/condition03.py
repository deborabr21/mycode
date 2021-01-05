#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string and input matches expected value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config")

#Before the program ends, always display message to the user
print("Exiting the script")

