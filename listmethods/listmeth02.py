#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

#Use insert() method to insert a new element in the list
proto.insert(0,"test")
print(proto)

#Use remove() method to remove an element from the list
proto.remove("http")
print(proto)

#Remove last element from the list
proto.pop()
print(proto)

#Get the index of an element
proto.index("ssh")

