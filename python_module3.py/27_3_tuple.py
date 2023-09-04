x=("priya","priti","sujata",23,45,65,45,67)

y=list(x)


y[-1] = "pritam"

x = tuple(y)
print(x)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
