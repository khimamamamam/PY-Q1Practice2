from pyscript import display

x = "Year" #string
y = 2025 #integer
z = 3.14 #float
a = True #boolean
b = ['student1', 'student2', 'student3'] #list
c = (1,2,3) #tuple
d = {1,2,3} #set w/ numbers
e = {'emerald', 'ruby', 'sapphire'} #set w/ string
f = {
    "name": "Heart",
    "age": "16",
    "description": "makulit"
} #dictionary

display('The data type of x is', type(x), target="div1") #display output in div 1
display(type(y), target="div1")
display(type(z), target="div1")
display(type(a), target="div1")
display(type(b), target="div1")
display(type(c), target="div1")
display(type(d), target="div1")
display(type(e), target="div1")
display(type(f), target="div1")
display(f["name"], f["description"])