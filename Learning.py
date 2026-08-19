# LIST COMPREHENSION
# new_list = [new_item for item in list]
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Naitik"
new_list = [letter for letter in name]
print(new_list)

doubled = [2*n for n in range(1,5)]
print(doubled)


# conditional list comprehension
# new_list = [new item for item in list if test]
names = ["alex", "Nats", "priks", "Naitik", "Harsh"]
short_name = [name for name in names if len(name)<5]
print(short_name)

uppercased = [name.upper() for name in names if len(name)>4]
print(uppercased)

#DICTIONARY COMPREHENSION
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
names = ["alex", "Nats", "priks", "Naitik", "Harsh"]
students_score= {student:random.randint(1,100) for student in names}
print(students_score)

passed_students = {student:score for (student,score) in students_score.items() if score>=60}
print(passed_students)

student_dict = {
    "student": ["Naitik" , "Harsh" , "NATS"],
    "score": [56,76,98]
}
import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)

# #looping through data frame
# for (key,value) in student_df.items():
#     print(key)
#     print(value)

#ITTEROWS : TO LOOP THROUGH ROWS RATHER THAN COLUMNS
for(index , row ) in student_df.iterrows():
    if row.student =="Naitik":
        print(row.score)


