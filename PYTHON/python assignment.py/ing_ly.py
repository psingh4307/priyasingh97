a=input("mystring:")
if len(a)>=3:
    a+="ing"
    print(a)
if a.endswith("ing"):
    a+="ly"
    print(a)
elif len(a)<=3:
    print("unchanged",a)

