#
#def functionname( parameters ):
#   "function_docstring"
#   function_suite
#   return [expression]
def SayHello( name):
    print("Hello! ",name)

SayHello('Ajay')    

# pass by ref vs Value
#All parameters (arguments) in the Python language are passed by reference
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)

# Function definition is here
def ReplaceAll( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
ReplaceAll( mylist );
print ("Values outside the function: ", mylist)


def Updatelist(list1,index,newValue):
    list1[index]=newValue;

print ("before update: ", mylist)
Updatelist(mylist,2,50)
print ("after update: ", mylist)

# arguments 
#required, keyword, default, Variable length
SayHello(name="ajay") # keyword
SayHello("ajay") #required , if you dont pass it it will throw error
def newfunc(defaultparam="ajay"):
    print(defaultparam)

newfunc() # it will print default name Ajay
newfunc("Raju") # print raju

# variable length param starts with *
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

