list_1=[25,34,35,22,24,34,12,11,14,15]
list_2=[25,34,11,15]
newlist=[]
'''for x in list_1:
    if x in list_2:
        
        newlist.append(x) 
print(newlist)'''

for x in list_2:
    if x in list_1:
        newlist.append(x)
print(newlist)

for x in list_1:
    if x in list_2:
        print("list contain sublist")

