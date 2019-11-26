first_name = ['sherman', 'martin', 'ray', 'joseph', 'ezra']
second_name = ['ochieng', 'omondi', 'odero', 'onyango', 'odhiambo']

# names_dict = {}
# for first_name, second_name in zip(first_name, second_name):
#     names_dict[first_name] = second_name

# print(names_dict)

names_dict_comp = {first: second for first, second in zip(first_name, second_name)}
print(names_dict_comp)