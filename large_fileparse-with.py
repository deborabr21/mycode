#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails

#return the number of success attempts
success = 0

#Display the IP number that failed
hackerz = []

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            hackerz.append(line.split(" ")[-1].rstrip("\n"))
        elif "-] Authorization failed" in line:
            success += 1

print("The number of failed log in attempts is", loginfail)
print(hackerz)
print("The number of successful log in attempts is", success)
