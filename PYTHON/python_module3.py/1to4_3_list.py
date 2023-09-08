#a)what is list? how will you reverse a list
''' ans) list is collection type which is used to store multiple items in single element.
a built -in function called reverse() is used to reverse the list.
this simple and quick way to reverse the list
syntax:- list_name.reverse()'''
#example
a = [1,3,4,56]

a.reverse()
print(a)

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist)
#second method

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist[::-1])




'''2)how will you remove last object from list?
ans) mylist.pop()
To delete the last element, we can use the negative index-1 . the 
use of the negative index allows us to delete the last element,
even without calculating the lenght of the list.'''
#example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.pop()
print(thislist)

# second method
thislist = ["banana", "Orange", "Kiwi", "cherry"]
del thislist[-1]
print(thislist)
#another method
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.remove("cherry")
print(thislist)

'''3) suppose list_1 is [2,33,222,14,25],what is list_1[-1]?
ans) list_1[-1] = 25 
'''
# [-1] is last item of list which is 25 or [-1]  is last index of list
list_1=[2,33,222,14,25]
list_1[-1]
print(list_1[-1])

'''
4)difference between append() and extend() method?
ans) append() adds a single element to the end of the list. 
whlie extend() can add multiple individual element to the end of the list'''

list_1=[2,33,222,14,25]
list_1.append(5) # add items last in list, in append method we can add only one items in list 
print(list_1)

list_1=[2,33,222,14,25]
thislist = ["banana", "Orange", "Kiwi", "cherry"]
list_1.extend  (thislist) # in extend method we can add two list and add more than one items
print(list_1) #To append elements from another list to the current list, use the extend() method.
