name : tuple[str,int,float] = ('pak',7,2.2) # immuteable 
last :int= 90
print(last)
print(name) # print
print(type(name)) # type
print(id(name)) # physcial address
print([i for i in dir(name) if "_" not in i]) # method and attributes

