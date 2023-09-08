# check whether a list contain a sublist

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

list=[[1,4,7,2],[2,3,4],[3,6,7]]
for x in list:
    print("sublist:",x)
else:
    print(list)