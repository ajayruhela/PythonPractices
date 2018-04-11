# creating list and accessng its items
#!/usr/bin/python


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

# update
list3 = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list [2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

# delete 
list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ")
#1997 will be deleted
print (list1)

# other operations
#Python Expression	Results	Description
#len([1, 2, 3])	3	Length
#[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
#['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
#3 in [1, 2, 3]	True	Membership
#for x in [1, 2, 3]: print x,	1 2 3	Iteration
print(len([1,2,3,4,5,6]))
print(list1 + list2)
print(['Hi!'] * 4)
print(3 in [1,2,3,4,5,6])
for x in [1,2,3,4] :
     print(x)

# indexing slicing and Mtrices
L = ['spam', 'Spam', 'SPAM!']
#Python Expression	Results	Description
#L[2]	'SPAM!'	Offsets start at zero
#L[-2]	'Spam'	Negative: count from the right
#L[1:]	['Spam', 'SPAM!']	Slicing fetches sections

print(L[2])
print(L[-2],"second from right")
print(L[1:])

# compare cmp is not available in Python3
list1, list2 = [123, 'xyz'], [123, 'xyz']
if list1==list2 : 
    print(True)

print('max:',max([2,5,8,4,1,0,-5,8]))
print('min:',min([2,5,8,4,1,0,-5,8]))
print('len:',len([2,5,8,4,1,0,-5,8]))

#dictionary

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict1['Name'])
print ("dict['Age']: ", dict1['Age'])
dtEmp= {'EmpId':'E1', 'Name': 'Zara', 'Age': 27}
dtComp= {'DeptId': 'D1', 'DeptName': 'Computer'}
obj ={'emp': dtEmp, 'dept': dtComp}
print (obj['emp']['EmpId'])
print (obj['emp']['Name'])
print (obj['emp']['Age'])
print (obj['dept']['DeptId'])
print (obj['dept']['DeptName'])

for x in obj.keys():
      for y in obj[x].keys():
          print(obj[x][y])

#
# Tuple
tuple1 =(1,2,3,4,5,6)
print(tuple1[2])
print(tuple1[-2])
print(tuple1[2:])
print('length: ',len(tuple1))
print('max: ',max(tuple1))
print('min: ',min(tuple1))
print('sum: ',sum(tuple1))
# can't update tuple[0]=5 
