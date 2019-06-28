from hotelfunctions import *
hotel = {
 '1': {
   '101': ['George Jefferson', 'Wheezy Jefferson'],
   '102': []
 },
 '2': {
   '237': ['Jack Torrance', 'Wendy Torrance'],
 },
 '3': {
   '333': ['Neo', 'Trinity', 'Morpheus']
 }
}

print("Would you like to check in or check out?")
usercheckin_out = input("Type 'in' or 'Out")
checkin(usercheckin_out)

print("What floor would you like?")
userfloor = input("type 1, 2, or 3")
floorrequest(userfloor)

print("how many occupants")
occupants = int(input("Enter up to two occupants"))
occupantnames =(input("first and last name"))
if floorrequest == '1':
    hotel['1']['102'] = occupantnames
    print(hotel)


"""def roomcheck():
    roomcheck = '  ' in hotel
    print("empty room")"""
"""print("which floor would you like to stay on?")
floorrequest("type 'first', 'second' or 'third'")
print("which room would you like?")
roomrequest = input("")
if inorout == 'in':
    #room emptiness check
    if room == values inside blank
        they can check in 
        for rooms in hotel:
    else 
        print("room is full")
if inorout == 'out':"""


