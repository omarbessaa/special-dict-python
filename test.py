import tp3



a = tp3.OrdrDict(cl1 = 12 , cl2 = 34)

print(a)
a['cl3'] = 544
a['cl4'] = 4
a['cl1'] = 0
a['cl3'] = -1
"""
print(a) \
del a['cl2'] \
print(a) \

print('cl1' in a ) \
print(len(a)) \
"""
b = tp3.OrdrDict(kk = -3 , lkl = -4)
a + b

i = iter(a)
print(a)
print(next(i))
print(next(i))

for i in a :
        print(a[i])
print(a.keys())
print(a.values())
print(a.items())
print('*************************************')
a.sort()
print(a)
a.reverse()
print(a)
