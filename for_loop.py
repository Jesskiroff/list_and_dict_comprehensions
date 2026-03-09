#For loop ex
numbers = [1, 2, 3, 4, 5]
new_numbers = []
for number in numbers:
    add_one = number + 1
    new_numbers.append(add_one)


#using list comprehension, we can take those 4 lines of code and put them into one line

# KeyboardInterrupt
# >>> name = "Jess"
# >>> letters = [letter for letter in name]
# >>> print(letters)
# ['J', 'e', 's', 's']
# >>> nums = range(1,5)
# >>> nums_list = [number for number in nums]
# >>> print(nums_list)
# [1, 2, 3, 4]
# >>> nums_list_times_two = [nums_list * 2]
# >>> print(nums_list_times_two)
# [[1, 2, 3, 4, 1, 2, 3, 4]]
# >>> nums_list_times_two = [nums_list]
# >>> nums_list_times_two = [nums_list + nums_list]
# >>> print(nums_list)
# [1, 2, 3, 4]
# >>> print(nums_list_times_two)
# [[1, 2, 3, 4, 1, 2, 3, 4]]
# >>> nums_list_times_two = nums_list
# >>> nums_list_times_two = [n * 2 for n in nums_list]
# >>> print(nums_list_times_two)

# > names = ["Alex", "Max", "Josh", "Jason", "Claire", "dave\
# "]
# >>> print(names)
# ['Alex', 'Max', 'Josh', 'Jason', 'Claire', 'dave']
# >>> short_names = [name for name in names if len(name) <5]
# >>> print(short_names)
# ['Alex', 'Max', 'Josh', 'dave']
# >>> 

# Something to return for item in list w more than 5 chars in caps 

# >>> cap_names = [name.upper() for name in names if len(name) > 5]
# >>> print(cap_names)


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
import random
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
# {'Alex': 66, 'Beth': 15, 'Caroline': 10, 'Dave': 60, 'Eleanor': 11, 'Freddie': 83}

