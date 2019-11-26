#finding squares of first 100 integers with list comprehensions
squares = [i**2 for i in range(1, 101)]

#finding remainders of squares of first 100 int divided by 5
remainder_5 = [i**2 % 5 for i in range(1, 101)]

#find names starting by A
names = ['Abel', 'Adam', 'Ben', 'Brian', 'Can', 'Cane', 'Dan', 'Ann']
names_a = [name for name in names if name.startswith('A')]

#find people born in 2010 and after
names_birth = [('Abel', 2010), ('Adam', 2009), ('Ben', 2008), ('Brian', 2015), ('Can', 2012), ('Cane', 2007), ('Dan', 2018), ('Ann', 2013)]
names_birth_2010 = [year for year in names_birth if year[1] >= 2010]
names_birth_2010_alt = [(name, year) for name, year in names_birth if year >= 2010]

#list scalar multiplication
values = [1, 2, 3, 4, 5]
mult_values = [4*val for val in values]

#caretsian product
A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]
cart_a_b = [(a, b) for a in A for b in B]
