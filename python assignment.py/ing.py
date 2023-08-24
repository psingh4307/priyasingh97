x=input("enter a string:")
if len(x)<3:
    print("unchanged")
if x.endswith("ing"):
    x+="ly"
elif len(x)>=3:
    x+="ing"
print(x)
