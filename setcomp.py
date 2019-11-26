nums = [1, 1, 2, 3, 4, 3, 5, 6, 5,2 , 3, 5, 8]

my_set = set()
for num in nums:
    my_set.add(num)
print(my_set)

my_set_comp = {num for num in nums}
print(my_set_comp)