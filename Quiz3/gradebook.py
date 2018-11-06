#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
modify this part accordingly!!!!
Created on Tue Oct 30 20:15:31 2018

@author: gokcol
for use in EE393 Oct.31 '2018 class study
"""

## Umut Çakan S006742 Computer Science

grades=dict();
f = open("gradebook.txt", "r")
firstLine=f.readline().rstrip()  #get the first line from the file
for line in f:  #read the rest of the file line by line
    line=line.rstrip() #remove \n at the end of each line
    c=line.split(":") #split each line into two parts
    #add each line to a dictionary - key is "name", value is "all grades (i.e. a list)
    grades[c[0]]=[ int(x) for x in (c[1].strip()).split(",")] 

print("** Student names and average grades **\n")

# Keep student names and average scores for later on.
average_grades = {}

# Print students and their average scores.    
for key, value in grades.items():
    average = sum(value) / len(value)
    print("Student:", key, "- Average:", average)
    average_grades[key] = average
    
print("\n** Max and Min grades of each section **\n")    

# Get MT1's max and min grade and print.
mt1_max_grade = max(grades.items(), key = lambda k: k[1][0])
mt1_min_grade = min(grades.items(), key = lambda k: k[1][0])    
print("MT1 max grade: ", mt1_max_grade[1][0])
print("MT1 min grade: ", mt1_min_grade[1][0])

# Get MT2's max and min grade and print.
mt2_max_grade = max(grades.items(), key = lambda k: k[1][1]) 
mt2_min_grade = min(grades.items(), key = lambda k: k[1][1])    
print("MT2 max grade: ", mt2_max_grade[1][1])
print("MT2 min grade: ", mt2_min_grade[1][1])


# Get F's max and min grade and print.
f_max_grade = max(grades.items(), key = lambda k: k[1][2])  
f_min_grade = min(grades.items(), key = lambda k: k[1][2])   
print("F max grade: ", f_max_grade[1][2])
print("F min grade: ", f_min_grade[1][2])
    
# Get HW's max and min grade and print.
hw_max_grade = max(grades.items(), key = lambda k: k[1][3])   
hw_min_grade = min(grades.items(), key = lambda k: k[1][3])  
print("HW max grade: ", hw_max_grade[1][3])
print("HW min grade: ", hw_min_grade[1][3])

# Get Quiz's max and min grade and print.
quiz_max_grade = max(grades.items(), key = lambda k: k[1][4])    
quiz_min_grade = min(grades.items(), key = lambda k: k[1][4])  
print("Quiz max grade: ", quiz_max_grade[1][4])
print("Quiz min grade: ", quiz_min_grade[1][4])

print("\n** Max and min values of the average scores **\n")

# Get Students' max and min average grade and print.
avg_max = max(average_grades.items(), key = lambda k: k[1])
avg_min = min(average_grades.items(), key = lambda k: k[1])
print("Max average:", avg_max[0], "- Grade(Average):", avg_max[1])
print("Min average:", avg_min[0], "- Grade(Average):", avg_min[1], "\n")  

# Save to a file.
try: 
    f = open("results.txt",'w',encoding = 'utf-8')
    # Save student names and average score.
    f.write("** Student names and average grades **\n\n") 
    for key, value in grades.items():
        average = sum(value) / len(value)
        f.write("Student: "+ key + " - Average: " + str(average) + "\n")
    # Save max and min evaluation types.
    f.write("\n** Max and Min grades of each section **\n\n") 
    f.write("MT1 max grade: " + str(mt1_max_grade[1][0]) + "\n")
    f.write("MT1 min grade: " + str(mt1_min_grade[1][0]) + "\n")
    f.write("MT2 max grade: " + str(mt2_max_grade[1][1]) + "\n")
    f.write("MT2 min grade: " + str(mt2_min_grade[1][1]) + "\n")
    f.write("F max grade: " + str(f_max_grade[1][2]) + "\n")
    f.write("F min grade: " + str(f_min_grade[1][2]) + "\n")
    f.write("HW max grade: " + str(hw_max_grade[1][3]) + "\n")
    f.write("HW min grade: " + str(hw_min_grade[1][3]) + "\n")
    f.write("Quiz max grade: " + str(quiz_max_grade[1][4]) + "\n")
    f.write("Quiz min grade: " + str(quiz_min_grade[1][4]) + "\n")
    f.write("\n** Max and min values of the average scores **\n\n")
    f.write("Max average: " + str(avg_max[0]) + " - Grade(Average): " + str(avg_max[1]) + "\n")
    f.write("Min average: " + str(avg_min[0]) + " - Grade(Average): " + str(avg_min[1]) + "\n")
# Close the file
finally:
    f.close()
    
## BONUS.

def search_student_name(student_name):
    # If student name exists, then print information.
    if student_name in grades.keys():
        student_grades = grades[student_name]
        print("\n** Information about " + student_name + ": **\n")
        print("MT1 Score:", student_grades[0])
        print("MT2 Score:", student_grades[1])
        print("F Score:", student_grades[2])
        print("HW Score:", student_grades[3])
        print("Quiz Score:", student_grades[4])
        print("Average Score:", sum(student_grades) / len(student_grades), "\n")
    else:
        print("\nERROR: Student name could not found. \n")

def get_student_name():
    student_name = input("Please enter student name: ")
    # Check if there is any integer in string or not.
    if any(letter.isdigit() for letter in student_name):
        print("\nERROR: Invalid student name, please do not use integer. \n")    
    else:
        search_student_name(student_name)
        

while True:
    # Print menu.
    print("** Menu **\n")
    print("1. View Student Information ")
    print("2. Exit ")
    selection = input("Please enter your choice: ")
    # Check if there is any integer in string or not.
    if selection == '1':
        get_student_name()
        continue
    elif selection == '2':
        print("Exiting.. Thank you.")
        break
    else:
        print("\nERROR: Invalid option please select proper one. \n")
        continue

# Get average scores' max and min grade and print.

#--------end of demo    
#Modifications that are needed to be done by the student
#-------------------------------------------------------
#1: Calculate averages for each of the students
#2: Max & Min values for each of the evaluation types (MT1, MT2, F, HW, Quiz)
#3: Max & Min values for the averages
#4: Output to a text file
#5: Use try-catch for catching possible file-related errors
#Submit via LMS
#Use built-in list and dictionary methods and functions (sum, max etc)
###BONUS ==> User enters a Student name and program returns all grades of that
# student and student average grade
#deadline: Oct 31, 23:59