

d = {1:"hello",2:"hello1",3:"hello2"}

print(type(d))

print(d.get(1))   #key answer value
print(d.keys())   #only key output
print(d.values()) #only value output
print(d.items())  #pair items output
d.update({4:"meet",5:"harsh"}) #update item add
print(d)          
d.pop(2)           # 2 key remove item
print(d)
d.popitem()        #last item remove
print(d)