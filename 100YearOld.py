import datetime

uname = input("Enter your name: ")
uage = input("Enter your age: ")
val = int(uage)
x = datetime.datetime.now()
y = 100 - (val)
print ("At ",x.year+y," your age will be 100")
