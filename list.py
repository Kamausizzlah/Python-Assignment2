my_list = []
print("Before Append:",  my_list)

my_list.extend([10, 20, 30, 40])
print("After Append:", my_list)

my_list[1] = 15
print("After Change:", my_list)

my_list.extend([50, 60, 70])
print("After Extend:", my_list)

del my_list[-1]
print("After Delete:", my_list)

my_list.sort()
print("After Sort:", my_list)

my_list.index(30)
print("Index of 30:", my_list.index(30))