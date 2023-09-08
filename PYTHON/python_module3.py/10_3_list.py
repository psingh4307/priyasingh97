#take two list and return true if they have atleast one common items

a=["a","b","c","d",1,2,3,4]
b=["a",56,5,1]



for x in a:
    if x in b :
        print(True)
    else:
        print(False)

for x in b:
    if x in a:
        print("true")
    else:
        print("false")



