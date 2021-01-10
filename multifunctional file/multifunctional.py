# Function 1 (lambda line ^ 2 )

squaring = lambda num: num ** 2
number = 11
print(f'{number} squared is {squaring(number)}')

# Function 2 ( powered list with map )

random_list = [5, 1, 16, 42, 14]

powered_list = list(map(lambda num: num ** 2, random_list))
print(f'{powered_list} _ this list is made by map function')

# Function 3 ( Powered list with comprehension )

comp_powered_list = [num ** 2 for num in random_list]
print(f'{comp_powered_list} _ this list is made by string comprehension')

# Function 4 ( compare and filter )

numbers_to_compare = [(2, 3), (23, 22), (101, 202), (777, 333), (16, 25)]

t = lambda num: num[0] > num[1]

compared_numbers = list(filter(lambda num: num[0] > num[1], numbers_to_compare))

print(f'{compared_numbers} _ presents only couples with greater first number')

# Function 5 ( Cool quote )

stark_quote = 'You have an army we have a hulk'

filtered_quote = list(filter(lambda word: word[0] not in 'aeiouy', stark_quote.split()))

print(filtered_quote)
