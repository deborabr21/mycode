#!/usr/bin/env python3
user_input = input("Please enter an IPv4 IP address:")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the IPv4 address is:", user_input)

#The first line should collect and store input from the user.
#Ask the user for the 'vendor name' associated with the device. 
#Use any variable name you would like.
user_input_two = input("Please enter the vendor name associated with the device: ")

#Use a second line of code to print the input you just collected from the user.
print("The vendor name associated with the device is: ", user_input_two)
