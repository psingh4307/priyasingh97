#replace  last value of tuple in a list

x=("priya","priti","sujata",23,45,65,45,67)

y=list(x)


y[-1] = "pritam"

x = tuple(y)
print(x)


