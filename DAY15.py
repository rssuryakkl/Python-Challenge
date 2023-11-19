#hii all this is DAY15(19-11-2023) today we are disscuss about function
#Calling a Function
def hi():
    print("hie")
print(hi())

#Passing Parameters in Functions
a=9
b=2
def add(a,b):
    print("Add")
    return a+b
print(add(a,b))

#Keyword Arguments
def data(name):
    print("Ente you name:",name)
data(name="rs")
#

def data(name,age):
    print("Ente you name:",name)
    print("Ente you age:",age)
data(age="90",name="rs")

#Default Arguments
def  defal(name,age="29"):
    print("Enter age:",age)
    print("Enter name:",name)
    return
defal("mani")
#

def sum(x,y,z):
    print("sum of three nos :",x+y+z)
sum(5,10,15)
#

def noss(*nos):
    for n in nos:
        print(n)
    return
noss(1,3)
noss(45,67,889)

# until this is rs bye















