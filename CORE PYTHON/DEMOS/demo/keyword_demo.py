import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


#1. str 
var='firstbit solution '
var="firstbit solution"
print(var)
print(type(var))



##sequential


#1. list 
var=[10,20,30,40]  
print(var)
print(type(var))


#2. tuple
var=(10,20,30,40)
print(var)
print(type(var))


#3. range 
var=range(1,10)
print(var)
print(type(var))




### set type 
#1. set
var={10,20,30,40}
print(var)
print(type(var))


#2. frozenset
var=frozenset({10,20,30,40})
print(var)
print(type(var))


#mapping 
#1. dict 
var={1:'python',2:'java',3:'c'}
print(var)
print(type(var))


 ###other
 #1. bool 
var=True
print(var)
print(type(var))


#2. Nonetype
var=None 
print(var)
print(type(var))
