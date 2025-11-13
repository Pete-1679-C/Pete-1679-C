# -*- coding: utf-8 -*-
"""
UTSA – Fall 2023 - CS1063 – Section 001 - Project 1 - written by PETE CHALLENGER
"""

def student_list1():
    for k,v in dict.items(student_body):
        print(k, ':', v)

def student_list2():
    for k,v in dict.items(student_body):
        print(f"{k}'s Exam Grade is {v:.1f}")
        
def menu_input():
    print('\nEnter From the List of Numbers from the Menu to Move Forward:')
    print('\nMenu:\n1 - List of Students and Grades')
    print('2 - Grade Report')
    print("3 - Modify a Student's Grade")
    print('4 - Quit the Program')

stop_program = False
print('Hello and Welcome.')

class_size = int(input('Please Enter Your Class Size: '))

student_body = {}
i = 1
while class_size <= 0:
    class_size = int(input('\nInvalid Number of Students. Please Try Again.\n'))
else:
    while (0 < i <= class_size): 
        name_validity = False
        student_names = input("\nPlease Enter a Student's First Name (and Last Name Optional) Here: ")
        while name_validity == False:
            for char in student_names:
                if not char.isalpha() and char != ' ' and char != '-' and char != "'":
                    student_names = input('\nInvalid Entry. Please Try Again.\n')
                else:
                    name_validity = True   
        
        student_grade = int(input("\nPlease Enter That Student's Exam Grade Here: "))
        i+= 1
    
        student_body[student_names] = student_grade
    
print('\nList of Class Students and Their Exam Grades:\n')
student_list1()
    
print("\nGreat. Now That We've Established Your Class and Your Student's Grades, What Would You Like to Do Now?")

while not stop_program:
    menu_input()
    menu_choice = int(input('\n'))
    
    if menu_choice == 1:
        print("\nYou Have Chosen Option 1 to View Your Student's Names and Grades.")
        print('Here is a List of Class Students and Their Exam Grades:\n')
        student_list2()
        print()
        
    elif menu_choice == 2:
        print("\nYou Have Chosen Option 2 to View Your Class' Grade Report.")
        
        A = 0
        B = 0
        C = 0
        D = 0
        F = 0
        
        for value in dict.values(student_body):
            if 90 <= value <= 100:
                A += 1
            elif 80 <= value < 90:
                B += 1
            elif 70 <= value < 80:
                C += 1
            elif 60 <= value < 70:
                D += 1
            else:
                F += 1
                
        print('Grade Report:')
        print('A: ', A)
        print('B: ', B)
        print('C: ', C)
        print('D: ', D)
        print('F: ', F)
        
    elif menu_choice == 3:
        print("\nYou Have Chosen Option 3 to Modify a Student's Grade.") 
        
        student_search = False
        name_search = input("Please Enter the Student's First Name (and Last Name if Inputted) Here: ")
        
        while student_search == False:
            if name_search not in student_body:
                name_search = input('Invalid Name. Please Try Again.\n')
            else:
                new_score = int(input("Enter the Student's New Grade Here: "))
                student_body[name_search] = new_score
                
                print(f"\n{name_search}'s New Grade is Now {student_body[name_search]}.")
                    
                student_search = True
                
    elif menu_choice == 4:
        print('\nYou Have Chosen Option 4 to Quit the Program.')
        print('This Program Will Now Close. Goodbye.')
        stop_program = True
        
    else:
        print('\nInvalid Choice. Please Try Again.')
            