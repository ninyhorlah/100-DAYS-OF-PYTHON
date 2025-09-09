import random

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]

print(new_list)

name = 'Angela'
new_name = [letter for letter in name]
print(new_name)

num = range(1,5)
new_num = [n*2 for n in num]
print(new_num)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = print([name for name in names if len(name) < 5])
long_names = print([name.upper() for name in names if len(name) > 5])

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)