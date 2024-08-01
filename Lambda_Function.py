# Lambda Function
#1.Write a lambda function that takes a string as input and returns a new string with all characters in uppercase.

str1="computer science"
str2=lambda str1:str1.upper()
print(str2(str1))

Output: COMPUTER SCIENCE
--------------------------------------------------------------------------------------------------------------------------


#2. Write a lambda function that takes a string as input and returns a new string with all vowels removed.

str="computer_science"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result=lambda str:''.join(c for c in str if c not in vowels)
print(result(str))

Output: cmptr_scnc

--------------------------------------------------------------------------------------------------------------------------
#3. Write a lambda function that takes a list of numbers and returns a new list with only even numbers. (Use filter)

numbers=[1,2,3,4,5,6,7,8,9,10]
result=lambda numbers:list(filter(lambda  x:x%2==0,numbers))
print(result(numbers))

Output: [2, 4, 6, 8, 10]

-------------------------------------------------------------------------------------------------------------------------------
#4. Write a lambda function that takes a list of numbers and returns the sum of all elements. (Use reduce)

from functools import reduce

numbers=[1,2,3,4,5,6,7,8,9,10]
result = lambda numbers: reduce(lambda x, y: x + y, numbers)
print(result(numbers))

Output: 55

#5. Write a lambda function that takes a list of strings and returns a new list with all strings sorted by length (shortest to longest).
strings = ["apple", "banana", "kiwi", "cherry", "date"]
result = lambda strings: sorted(strings, key=lambda s: len(s))
print(result(strings)) 

Output: ['kiwi', 'date', 'apple', 'banana', 'cherry']

