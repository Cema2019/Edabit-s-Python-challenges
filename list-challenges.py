"""
1. Find the Largest Number in a List
Create a function that takes a list of numbers. Return the largest number in
the list.
Examples:
findLargestNum([4, 5, 1, 3]) ➞ 5
findLargestNum([300, 200, 600, 150]) ➞ 600
findLargestNum([1000, 1001, 857, 1]) ➞ 1001
"""

def findLargestNum(nums):
	return max(nums)

# *************************************************************
"""
2. Get the Sum of All List Elements
Create a function that takes a list and returns the sum of all numbers in
the list.

Examples:
get_sum_of_elements([2, 7, 4]) ➞ 13
get_sum_of_elements([45, 3, 0]) ➞ 48
get_sum_of_elements([-2, 84, 23]) ➞ 105
"""

def get_sum_of_elements(lst):
	return sum(lst)

# *************************************************************
"""
3. Pair Management
Given two arguments, return a list which contains these two arguments.

Examples:
make_pair(1, 2) ➞ [1, 2]
make_pair(51, 21) ➞ [51, 21]
make_pair(512124, 215) ➞ [512124, 215]
"""

def make_pair(num1, num2):
	return [num1, num2]

# *************************************************************
"""
4. Even or Odd?
Given a list of integers, determine whether the sum of its elements is even
or odd.
The return value should be a string ("odd" or "even").
If the input list is empty, consider it as a list with a zero ([0]).
Examples:
even_or_odd([0]) ➞ "even"
even_or_odd([1]) ➞ "odd"
even_or_odd([]) ➞ "even"
even_or_odd([0, 1, 5]) ➞ "even"
"""

def even_or_odd(lst):
	return "even" if sum(lst) % 2 == 0 else "odd"

# **************************************************************
"""
5. Check if a List Contains a Given Number
Write a function to check if a list contains a particular number.
Examples:
check([1, 2, 3, 4, 5], 3) ➞ True
check([1, 1, 2, 1, 1], 3) ➞ False
check([5, 5, 5, 6], 5) ➞ True
check([], 5) ➞ False
"""

def check(lst, el):
	return el in lst

# *************************************************************
"""
6. Fix the Errors / Comparing Arrays
Programmer Pete is trying to create a function that returns True if
two lists share the same length and have identical numerical values
at every index, otherwise, it will return False.
However, the solution his function gives is in an unexpected format. Can you
fix Pete's function so that it behaves as seen in the examples below?
Examples:
check_equals([1, 2], [1, 3]) ➞ False
check_equals([1, 2], [1, 2]) ➞ True
check_equals([4, 5, 6], [4, 5, 6]) ➞ True
check_equals([4, 7, 6], [4, 5, 6]) ➞ False
check_equals([1, 12], [11, 2]) ➞ False
"""

def check_equals(lst1, lst2):
	return lst1 == lst2

# *************************************************************
"""
7. Buggy Code (Part 3)
Fix the code in the code tab to pass this challenge (only syntax errors).
Look at the examples below to get an idea of what the function should
do.
Examples:
sum_lst([1, 2, 3, 4, 5]) ➞ 15
sum_lst([-1, 0, 1]) ➞ 0
sum_lst([0, 4, 8, 12]) ➞ 24
"""

def sum_lst(lst):
	total = 0
	for i in lst:
		total += i
	return total

# *************************************************************
"""
8. Find the Smallest and Biggest Numbers
Create a function that accepts a list of numbers and return both the minimum
and maximum numbers, in that order (as a list).
Examples:
min_max([1, 2, 3, 4, 5]) ➞ [1, 5]
min_max([2334454, 5]) ➞ [5, 2334454]
min_max([1]) ➞ [1, 1]
"""

def min_max(nums):
	return [min(nums), max(nums)]

# *************************************************************
"""
9. Return the First and Last Elements in a List
Create a function that takes a list of values and returns
the first and last values in a new list.
Examples:
first_last([5, 10, 15, 20, 25]) ➞ [5, 25]
first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True]
first_last([None, 4, "6", "hello", None]) ➞ [None, None]
"""

def first_last(lst):
	return [lst[0], lst[-1]]

# *************************************************************
"""
10. Destructuring Lists III
# DO NOT change arr
# DO NOT USE lips = arr[2]
# "eyes", "nose", and "ears" should not be assigned to anything
"""

arr = ["eyes", "nose", "lips", "ears"]
# The solution uses iterable unpacking with underscores for ignored elements.
_, _, lips, _ = arr

# *************************************************************
"""
11. Iterable Unpacking
There is an easy way to assign to array values to the nth index by using
the Rest element.
head, tail = [1, 2, 3, 4]
print(head) ➞ 1
print(tail) ➞ 2
But how could I make tail = [2, 3, 4] instead of tail = 2?
Add something into the code and make this happen.
"""

# The solution uses the star operator (*) for extended unpacking.
head, *tail = [1, 2, 3, 4]

# *************************************************************
"""
12. Check if All Values Are True
Create a function that returns True if all parameters are truthy, and False otherwise.
Examples:
all_truthy(True, True, True) ➞ True
all_truthy(True, False, True) ➞ False
all_truthy(5, 4, 3, 2, 1, 0) ➞ False
"""

def all_truthy(*args):
	return all(args)

# *************************************************************
"""
13. Return Last Item
Create a function that returns the last value of the last item in a list or
string.
Examples:
last_ind([0, 4, 19, 34, 50, -9, 2]) ➞ 2
last_ind("The quick brown fox jumped over the lazy dog") ➞ "g"
last_ind([]) ➞ None
"""

def last_ind(lst):
	return lst[-1] if lst else None

# *************************************************************
"""
14. Convert All List Items to String
Create a function that takes a list of integers and strings. Convert
integers to strings and return the new list.
Examples:
parse_list([1, 2, "a", "b"]) ➞ ["1", "2", "a", "b"]
parse_list(["abc", 123, "def", 456]) ➞ ["abc", "123", "def", "456"]
parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]) ➞ ["1", "2", "3", "17", "24", "3", "a", "123b"]
parse_list([]) ➞ []
"""

def parse_list(lst):
    return list(map(str, lst))

# *************************************************************
"""
15. Sandwich Fillings
Given a sandwich (as a list), return a list of fillings inside the sandwich. This
involves ignoring the first and last elements.
Examples:
get_fillings(["bread", "ham", "cheese", "ham", "bread"]) ➞ ["ham", "cheese", "ham"]
get_fillings(["bread", "sausage", "tomato", "bread"]) ➞ ["sausage", "tomato"]
get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]) ➞ ["lettuce", "bacon", "tomato"]
"""

def get_fillings(sandwich):
	_, *fillings, _ = sandwich
	return fillings

# *************************************************************
"""
16. Sum Greater Than Five
Write a function that returns the sum of elements greater than 5, in the
given list.
Examples:
sum_five([1, 5, 20, 30, 4, 9, 18]) ➞ 77
sum_five([1, 2, 3, 4]) ➞ 0
sum_five([10, 12, 28, 47, 55, 100]) ➞ 252
"""

def sum_five(lst):
	return sum(list(filter(lambda x: x > 5, lst)))

# *************************************************************
"""
17. Sort Numbers in Ascending Order
Examples:
sort_nums_ascending([1, 2, 10, 50, 5]) ➞ [1, 2, 5, 10, 50]
sort_nums_ascending([80, 29, 4, -95, -24, 85]) ➞ [-95, -24, 4, 29, 80, 85]
sort_nums_ascending([]) ➞ []
"""

def sort_nums_ascending(lst):
	return sorted(lst)

# *************************************************************
"""
18. Find the Index
Create a function that takes a list and a string as arguments and returns
the index of the string.
Examples:
find_index(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2
find_index(["Red", "blue", "Blue", "Green"], "blue") ➞ 1
find_index(["a", "g", "y", "d"], "d") ➞ 3
find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") ➞ 0
"""

def find_index(lst, txt):
	return lst.index(txt)

# *************************************************************
"""
19. Find None in a List
Create a function to find None in a list of numbers. The return value should be the index where None is
found. If None is not found in the list, then return -1.
Examples:
find_none([1, 2, None]) ➞ 2
find_none([None, 1, 2, 3, 4]) ➞ 0
find_none([0, 1, 2, 3, 4]) ➞ -1
"""

def find_none(lst):
	return lst.index(None) if None in lst else -1

# *************************************************************
"""
20. The Forbidden Letter
Given a letter and a list of words, return whether the letter does not appear in any of the words.
Examples:
forbidden_letter("r", ["rock", "paper", "scissors"]) ➞ False
forbidden_letter("a", ["spoon", "fork", "knife"]) ➞ True
forbidden_letter("m", []) ➞ True
"""

def forbidden_letter(char, lst):
	return all(char not in word for word in lst)

# *************************************************************
"""
21. Summing a Slice
Given a list and an integer n, return the sum of the first n numbers
in the list.
Worked Example:
sum_first_n_nums([9, 8, 7, 6], 3) ➞ 24
The parameter n is specified as 3.
The first 3 numbers in the list are 9, 8 and 7.
The sum of these 3 numbers is 24 (9 + 8 + 7).
Return the answer.
Examples:
sum_first_n_nums([1, 3, 2], 2) ➞ 4
sum_first_n_nums([4, 2, 5, 7], 4) ➞ 18
sum_first_n_nums([3, 6, 2], 0) ➞ 0
"""

def sum_first_n_nums(lst, n):
	return sum(lst[:n])

# *************************************************************
"""
22. List From a Range of Numbers
Create a function that returns a list of all the integers between two given
numbers start and end.
Examples:
range_of_num(2, 4) ➞ [3]
range_of_num(5, 9) ➞ [6, 7, 8]
range_of_num(2, 11) ➞ [3, 4, 5, 6, 7, 8, 9, 10]
"""

def range_of_num(start, end):
	return list(range(start + 1, end))

# *************************************************************
"""
23. Get the File Name
Create a function that returns the selected filename from a path. Include the extension in
your answer.
Examples:
get_filename("C:/Projects/pil_tests/ascii/edabit.txt") ➞ "edabit.txt"
get_filename("C:/Users/johnsmith/Music/Beethoven_5.mp3") ➞ "Beethoven_5.mp3"
get_filename("ffprobe.exe") ➞ "ffprobe.exe"
"""

def get_filename(path):
	return path.split("/").pop()

# *************************************************************
"""
24. Less Than, Greater Than
Create a function that takes two numbers num1, num2, and a list lst and
returns a list containing all the numbers in lst greater than num1 and
less than num2.
Examples:
list_between(3, 8, [1, 5, 95, 0, 4, 7]) ➞ [5, 4, 7]
list_between(1, 10, [1, 10, 25, 8, 11, 6]) ➞ [8, 6]
list_between(7, 32, [1, 2, 3, 78]) ➞ []
"""

def list_between(num1, num2, lst):
	return list(filter(lambda x: x > num1 and x < num2, lst))

# *************************************************************
"""
25. Convert a List to a String
Create a function that takes a list of numbers or letters and returns a
string.
Examples:
list_to_string([1, 2, 3, 4, 5, 6]) ➞ "123456"
list_to_string(["a", "b", "c", "d", "e", "f"]) ➞ "abcdef"
list_to_string([1, 2, 3, "a", "s", "dAAAA"]) ➞ "123asdAAAA"
"""

def list_to_string(lst):
	# Alternative using list comprehension: return "".join(str(x) for x in lst)
    return "".join(map(str, lst))

# *************************************************************
"""
26. How Much is True?
Create a function which returns the number of True values in a list.
Examples:
count_true([True, False, False, True, False]) ➞ 2
count_true([False, False, False, False]) ➞ 0
count_true([]) ➞ 0
"""

def count_true(lst):
	return lst.count(True)

# *************************************************************
"""
27. Find the Second Largest Number
Create a function that takes a list of numbers and returns the second largest number.
Examples:
second_largest([10, 40, 30, 20, 50]) ➞ 40
second_largest([25, 143, 89, 13, 105]) ➞ 105
second_largest([54, 23, 11, 17, 10]) ➞ 23
"""

def second_largest(lst):
	return sorted(lst)[-2]

# *************************************************************
"""
28. Number to Reversed Array
Create a function that takes a number and returns a list with the digits of
the number in reverse order.
Examples:
reverse_list(1485979) ➞ [9, 7, 9, 5, 8, 4, 1]
reverse_list(623478) ➞ [8, 7, 4, 3, 2, 6]
reverse_list(12345) ➞ [5, 4, 3, 2, 1]
"""

def reverse_list(num):
	return list(map(int, str(num)))[::-1]

# *************************************************************
"""
29. Zip It, If You Can?
Given a list of women and a list of men, either:
Return "sizes don't match" if the two lists have different sizes.
If the sizes match, return a list of pairs, with the first woman paired
with the first man, second woman paired with the second man, etc.
Examples:
zip_it(["Elise", "Mary"], ["John", "Rick"]) ➞ [("Elise", "John"), ("Mary", "Rick")]
zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh"]) ➞ "sizes don't match"
zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh", "Tim"]) ➞ [("Ana", "Bob"), ("Amy", "Josh"), ("Lisa", "Tim")]
"""

def zip_it(women, men):
	return ("sizes don't match" if len(women) != len(men)
					else list(zip(women, men)))

# *************************************************************
"""
30. Rotate the List by One
Given a list, rotate the values clockwise by one (the last value is sent to
the first position).
Check the examples for a better understanding.
Examples:
rotate_by_one([1, 2, 3, 4, 5]) ➞ [5, 1, 2, 3, 4]
rotate_by_one([6, 5, 8, 9, 7]) ➞ [7, 6, 5, 8, 9]
rotate_by_one([20, 15, 26, 8, 4]) ➞ [4, 20, 15, 26, 8]
"""

def rotate_by_one(lst):
    return lst[-1:] + lst[:-1]

# *************************************************************
"""
31. Array of Word Lengths
Create a function that takes a list of words and transforms it into a list
of each word's length.
Examples:
word_lengths(["hello", "world"]) ➞ [5, 5]
word_lengths(["Halloween", "Thanksgiving", "Christmas"]) ➞ [9, 12, 9]
word_lengths(["She", "sells", "seashells", "down", "by", "the", "seashore"]) ➞ [3, 5, 9, 4, 2, 3, 8]
"""

def word_lengths(lst):
	return list(len(x) for x in lst)

# *************************************************************
"""
32. Even Index Elements in a List
Create a function that takes a list of integers and returns the sum of all
the integers that have an even index, multiplied by the integer at
the last index.
For example:
[2, 3, 4, 5] ➞ 30
(2 + 4) * 5 ➞ 30
[1, 4, 5, 6, 7, 2, 3] ➞ 48
(1 + 5 + 7 + 3) * 3 ➞ 48
Examples:
even_last([]) ➞ 0
even_last([1, 3, 3, 1, 10]) ➞ 140
even_last([-11, 3, 3, 1, 10]) ➞ 20
"""

def even_last(lst):
	return 0 if len(lst) == 0 else sum(lst[::2]) * lst[-1]

# *************************************************************
"""
33. Largest Numbers
Create a function that takes two arguments of a list of numbers lst and
a constant number n and returns the n largest numbers from
the given list.
Examples:
largest_numbers(2, [4, 3, 2, 1]) ➞ [3, 4]
largest_numbers(1, [7, 19, 4, 2]) ➞ [19]
largest_numbers(3, [14, 12, 57, 11, 18, 16]) ➞ [16, 18, 57]
largest_numbers(0, [1, 3, 4, 2]) ➞ []
"""

def largest_numbers(n, lst):
	return [] if n == 0 else sorted(lst)[-n:]

# *************************************************************
"""
34. Find the Index (Part #2)
Create a function that searches for the index of a given item in a list. If
the item is present, it should return the index, otherwise, it should
return -1.
Examples:
search([1, 2, 3, 4], 3) ➞ 2
search([2, 4, 6, 8, 10], 8) ➞ 3
search([1, 3, 5, 7, 9], 11) ➞ -1
"""

def search(lst, item):
	return -1 if item not in lst else lst.index(item)

# *************************************************************
"""
35. Word Endings
Create a function that adds a string ending to each member in a list.
Examples:
add_ending(["clever", "meek", "hurried", "nice"], "ly") ➞["cleverly", "meekly", "hurriedly", "nicely"]
add_ending(["new", "pander", "scoop"], "er") ➞["newer", "panderer", "scooper"]
add_ending(["bend", "sharpen", "mean"], "ing") ➞["bending", "sharpening", "meaning"]
"""

def add_ending(lst, ending):
	# Alternative using f-string: return [f"{l}{ending}" for l in lst]
	return [str(l) + ending for l in lst]

# *************************************************************
"""
36. Hitting the Jackpot
Create a function that takes a list (slot machine outcome) and
returns True if all elements in the list are identical, and False otherwise.
The list will contain 4 elements.
Examples:
test_jackpot(["@", "@", "@", "@"]) ➞ True
test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
test_jackpot(["&&", "&", "&", "&&&&"]) ➞ False
test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False
"""

def test_jackpot(result):
	return all(x == result[0] for x in result)

# *************************************************************
"""
37. Unlucky 13
Given a sorted list of numbers, remove any numbers that are divisible by 13. Return the amended list.
Examples:
unlucky_13([53, 182, 435, 591, 637]) ➞ [53, 435, 591]
# 182 and 637 are divisible by 13.
unlucky_13([24, 316, 393, 458, 1279]) ➞ [24, 316, 393, 458, 1279]
# No numbers in the list are divisible by 13.
unlucky_13([104, 351, 455, 806, 871]) ➞ []
# All numbers in the list are divisible by 13.
"""

def unlucky_13(nums):
	return list(filter(lambda x: x % 13 != 0, nums))

# *************************************************************
"""
38. Get the File Extension
Write a function that maps files to their extension names.
Examples:
get_extension(["code.html", "code.css"]) ➞ ["html", "css"]
get_extension(["project1.jpg", "project1.pdf", "project1.mp3"]) ➞ ["jpg", "pdf", "mp3"]
get_extension(["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"]) ➞ ["rb", "cpp", "py", "js"]
"""

def get_extension(lst):
	return [s.split(".")[-1] for s in lst]
