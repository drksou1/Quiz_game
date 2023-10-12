#! /usr/bin/python3

t=(1,3,5)
t=1,2,3,4,5,5,7
print(t)

single_element_tuple=(4,)
print(single_element_tuple)

t=(1,4,66,3)
print(t[2:3])

t1=(4,6,10)
t3=t1+t
print(t3)

#repetition, repeating the tuple
t_repeat=t1*3
print(t_repeat)

#membership
print(4 in t1)

#length
print(len(t1))

#unpacking
a,b,c=t1
print(a,b,c)

#tuple methods
t1.index(10)
t_repeat.count(10)

#multiple return values, functions can return multiple tuples
def get_info():
    return 'Sara', 39
name,age=get_info()
all=get_info()
print(all)

#iterating over pairs
for a, b in zip((1,2,3),(4,5,6)):
    print(a,b)

for index, value in enumerate(('a','b','c')):
    print(index,value)

#can touples change? list inside a touple can
t_change=(1,2,3,4,[3,4,5,6])
t_change[-1][-2]=555
print(t_change)

#other way
t_change[-1].append(34)
print(t_change)