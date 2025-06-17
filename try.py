school = "Central Uni"

def username(myname):
    name = myname
    username1 = "My name is " + name
    return username1

showname = username(myname="Ghana")

african_countries = ["Ghana", "Nigeria", "Congo", "Somalia"]

for country in african_countries:
    if country == "Nigeria":
        print(showname)
    else:
        print('no')







