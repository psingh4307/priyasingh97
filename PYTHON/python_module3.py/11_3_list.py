# generate and print list of square number between 1 to 30 and print first and last 5 items from square list

squared_list = []
for i in range(1,30):
    squared_list.append(i*i)
print(squared_list)

print(squared_list[0:6])
print(squared_list[-6:-1])

