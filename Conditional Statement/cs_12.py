# -*- coding: utf-8 -*-
"""CS-12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nowGHsQLKNtRIyfb4MVNRB1fEXs1OFJj

Write a program to read roll no, name and marks of three subjects and calculate the total, percentage and division. 

Test Data :
Input the Roll Number of the student :784
Input the Name of the Student :James
Input the marks of Physics, Chemistry and Computer Application : 70 80 90
Expected Output :
Roll No : 784
Name of Student : James
Marks in Physics : 70
Marks in Chemistry : 80
Marks in Computer Application : 90
Total Marks = 240
Percentage = 80.00
Division = First
"""

name = input("Enter your name: ")
roll = int(input("Enter your roll: "))
marks1= float(input("Enter your marks in physics: "))
marks2= float(input("Enter your marks in chemistry: "))
marks3= float(input("Enter your marks in computer application: "))

total_marks = marks1+marks2+marks3
percentage = total_marks//3

if (percentage>=60):
	 division = 'first'
elif (percentage<60 and percentage>=48):
     division = 'second'
elif(percentage<48 and percentage>=36):
    division = 'pass'
else:
	division = 'fail'

print("Roll: ",roll)
print("Name: ",name)
print("Marks in physics: ",marks1)
print("Marks in chemistry: ",marks2)
print("Marks in computer application: ",marks3)
print("Total: ",total_marks)
print("Percentage: ",percentage)
print("Division: ",division)