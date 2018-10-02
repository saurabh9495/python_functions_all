list = [1,2,3,4,5,6,7,8,9,0]
rlist = reversed(list)
tuple = ('a','b','c','d','e')
rtuple = reversed(tuple)
for i in rlist:
    print(i)
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
for i in rtuple:
    print(i)
# e
# d
# c
# b
# a