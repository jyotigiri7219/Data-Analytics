a = [5,4,5,4,5]
a[2] = 7
a[3] = 8
a[4] = 9
[1] = 6 # ek value se dusre value ko replace karne ko multimeals khate hai
print(a)

# reference copy
a =  [5,6,8,2,4]
b = a      # a ke ke value ko reference se b ki value ko change kar rhe h but a or b dono chnge ho raha h
b[0] = 100
print(a)
print(b)

# shallow copy
c = a.copy()  # a ke ke value ko shallow copy se c ki value ko change kar rhe h but a or c dono chnge nahi ho raha h
c[0] = 200
print(a)
print(c)

v = [10,20,30,40,50,60]
for i in v:
    print(i)

z = [100,200,300,400,500]
for i in range(len(z)):
    print(z[i])
