#!/usr/bin/env python3
icecream= ["flavors", "salty"]
icecream.append(99)
name =input ("What is your name? ")

#F-STRING
print(f"{icecream[-1]} flavors and {name} chooses to be {icecream[-2]}.")

#MIX AND MATCH
print(icecream[2], icecream[0] + " and", name , "chooses to be ", icecream[1])

#PRINT OBJECTS
print(icecream[2], "flavors, and ", name, " chooses to be salty.")
