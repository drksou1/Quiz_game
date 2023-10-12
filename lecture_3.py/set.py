#! /usr/bin/python3
s={1,2,3,4}

my_set={1,2,4,5}
my_set={1,2,4,5,5}
print(my_set)


#to add elements to the set ----------------------
my_set.add(9)
print(my_set)

my_set.update([10,11,12])
print(my_set)

#to remove elements to the set--------------------
my_set.remove(9)
print(my_set)

my_set.discard(4)
print(my_set)

#SET OPERATIONS 
# union():
a={1,2,'a',4}
b={5,'b',7,8}
c=a.union(b)
print(c)

# intersecion(): 
d=a.intersection(b)
print(d)

# difference(): 
e=a.difference(b)
print(e)

# symmeric_difference():
f=a.symmetric_difference(b)
print(f)


#DICIONARIES---------------- two ways ---------------
my_dict={'name': 'Paul', 
         'age':'30', 
         'city':'Pori'}
print(my_dict)

my_dict2=dict(name='Paul', age=30, city='Pori')
print(my_dict2)

#Accessing elements from the dictionary
print(my_dict['name']) #No
print(my_dict.get('Place')) #Yes
print(my_dict.get('name')) #Yes

#Modifying dictionary
my_dict['ag']=35 
print(my_dict)

my_dict['job']='engineer' #adding job to dicionary
print(my_dict)

#Rermoving elements
del my_dict['ag']
print(my_dict)

#iterating through keys
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)

#iterating through key value parts
for key, value in my_dict.items():
    print(key, value)

#Chenking if keys exist:
if 'name' in my_dict:
    print('name is present in dictionary')

#dicionary comprehension
squares={x:x*x for x in range(8)}
print(squares)