mylist = [1,1,1]
x = all(mylist)

mytuple = (0,True,False)
y = all(mytuple)

myset = {1,1,1}
z = all(myset)

mydict = {0:"Hello",1:"Python",2:"Learning"}
a = all(mydict)

print(x, y, z, a)
#True False True False