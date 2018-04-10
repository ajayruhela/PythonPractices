#!/usr/bin/python
a=20
b=20
a
b
if(a is b):

    print("true")
else:

    print("false")

if(id(a) is id(b)):

    print("true")
else:

    print("false")   

b=30
b
if(a is b):

    print("true")
else:

    print("false")

if(id(a) is id(b)):

    print("true")
else:
    
    print("false") 