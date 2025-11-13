# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import csv

def check_student_abc123():
    abc123_validity = False
    abc123_input = input('Please Provide abc123 of Student: \n')
    while not abc123_validity:
        try:
            if abc123_input in student_gradebook['Student\'s ABC123'].values:
                print('\nStudent abc123 Found')
                abc123_validity = True
            else:
                raise ValueError('\nError: Provided Student abc123 Not Found')
        except ValueError as excpt:
            print(excpt)
            abc123_input = input('Please Re-Enter a New Valid ID: \n')
    return abc123_input

def student_identifier():
    student_row = student_gradebook[student_gradebook['Student\'s ABC123'] == abc123_input]
    student_info = student_row[['First Name', 'Last Name']].values.tolist()[0]

    print(f'{student_info[0]} {student_info[1]}', end = '')

def list_exams():
    student_row = student_gradebook[student_gradebook['Student\'s ABC123'] == abc123_input]
    list_exams = [col for col in student_row if col.startswith('Exam')]
    list_grades = student_row[list_exams].values.tolist()[0]
    
    for v in list_grades:
        print(v, end = ' ')

def cal_ave1():
    student_row = student_gradebook[student_gradebook['Student\'s ABC123'] == abc123_input]
    list_exams = [col for col in student_row if col.startswith('Exam')]
    list_grades = student_row[list_exams].values.tolist()[0]
    student_avg = round(sum(list_grades) / len(list_grades))
    
    return student_avg

def cal_ave2():
    list_avg = []
    for i in range(len(student_gradebook)):
        total_exams = []
        for col in student_gradebook:
            if col.startswith('Exam'):
                exam = student_gradebook.loc [i, col]
                total_exams.append(exam)
        
        avg = round(sum(total_exams) / len(total_exams))
        list_avg.append(avg)
    
    return list_avg

def cal_low():
    student_row = student_gradebook[student_gradebook['Student\'s ABC123'] == abc123_input]
    list_exams = [col for col in student_row if col.startswith('Exam')]
    list_grades = student_row[list_exams].values.tolist()[0]
    min_grade = min(list_grades)
    
    return min_grade

def cal_high():
    student_row = student_gradebook[student_gradebook['Student\'s ABC123'] == abc123_input]
    list_exams = [col for col in student_row if col.startswith('Exam')]
    list_grades = student_row[list_exams].values.tolist()[0]
    max_grade = max(list_grades)
    
    return max_grade

def menu_input():
    print('Enter From the List of Numbers to Move Forward: \n')
    print('Menu: \n1 - List of Student\'s Exam Scores')
    print('2 - Grade Graphs')
    print('3 - Class Grade Graphs')
    print('4 - Output File')
    print('5 - Quit the Program\n')

def submenu_input():
    print('\nEnter From the List of Numbers to Move Forward: \n')
    print('Menu: \n1 - List All Exam Scores')
    print('2 - Average Exam Score')
    print('3 - Lowest Exam Score')
    print('4 - Highest Exam Score')
    print('5 - Exit Back to Main Program\n')
    
with open('section1-students.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile)
    
    gradebook = []
    
    for rows in csvfile:
        student_info = csvfile.readlines()
        for line in student_info:
            tokens = line.split(',')
            array = ([])
            for token in tokens:
                new_token = token.strip('\n')
                array.append(new_token)
            gradebook.append(array)

    student_gradebook = pd.DataFrame(
        data = (gradebook),
        columns = ['Student\'s ABC123', 'First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
    student_gradebook = student_gradebook.astype({'Exam 1' : int, 'Exam 2' : int, 'Exam 3' : int})

stop_program = False
stop_subprogram = False

while not stop_program:
    menu_input()
    try:
        menu_choice = input()
        if menu_choice == '1':
            print('\nYou Have Chosen Option 1 to View a Student\'s Exam Scores')
            abc123_input = check_student_abc123()
            while not stop_subprogram:
                submenu_input()
                try:
                    submenu_choice = input()
                    if submenu_choice == '1':
                        print('\nYou Have Chosen to View All of a Student\'s Exam Scores.\n')
                        student_identifier()
                        print(' has the Following Exam Scores:', end = ' ')
                        list_exams()
                    
                    elif submenu_choice == '2':
                        print('\nYou Have Chosen to View a Student\'s Average Exam Scores.\n')
                        student_identifier()
                        print(' has an Average Grade Score of:', end = ' ')
                        print(cal_ave1())
                    
                    elif submenu_choice == '3':
                        print('\nYou Have Chosen to View a Student\'s Lowest Exam Score.\n')
                        student_identifier()
                        print('\'s Lowest Exam Score is:', end = ' ')
                        print(cal_low())
                    
                    elif submenu_choice == '4':
                        print('\nYou Have Chosen to View a Student\'s Highest Exam Score.\n')
                        student_identifier()
                        print('\'s Highest Exam Score is:', end = ' ')
                        print(cal_high())
                    
                    elif submenu_choice == '5':
                        print('\nYou Have Chosen to Exit this Sub-Menu.')
                        print('Exiting Back to Main Program.\n')
                        break
                    
                    else:
                        raise ValueError('Invalid Input.')
                
                except ValueError as excpt:
                    print(f'\n{excpt}')
                    print('You Either Entered an Invalid Number or You Entered a Word or Character Instead.')
                    print('Please Try Again.')
        
        elif menu_choice == '2':
            print('\nYou Have Chosen Option 2 to View a Graph of a Student\'s Exam Scores.')
            abc123_input = check_student_abc123()
            
            student_row = student_gradebook[student_gradebook['Student\'s ABC123'] == abc123_input]
            student_info = student_row[['First Name', 'Last Name']].values.tolist()[0]
            
            list_exams = [col for col in student_row if col.startswith('Exam')]
            list_grades = student_row[list_exams].values.tolist()[0]
            
            student_dict = dict(zip(list_exams, list_grades))
            
            exams = list(student_dict.keys())
            grades = list(student_dict.values())
            
            plt.plot(exams, grades, color = 'r')
            plt.title('Report of Student Exam Grades', fontsize = 20)
            plt.xlabel('Exams', fontsize = 14)
            plt.ylabel('Scores', fontsize = 14)
            plt.ylim([0, 110])
            plt.legend([abc123_input], loc = 'upper right')
            plt.savefig(f'Report of Exam Grades for {student_info[0]} {student_info[1]}.png')
            plt.close()
            
        
        elif menu_choice == '3':
            print('\nYou Have Chosen Option 3 to Create a Graph of your Class\' Letter Grades.')
            
            letter_averages = {
                'A' : 0,
                'B' : 0,
                'C' : 0,
                'D' : 0,
                'F' : 0
            }
            
            for v in cal_ave2():
                if 90 <= v <= 100:
                    letter_averages['A'] += 1
                elif 80 <= v < 90:
                    letter_averages['B'] += 1
                elif 70 <= v < 80:
                    letter_averages['C'] += 1
                elif 60 <= v < 70:
                    letter_averages['D'] += 1
                else:
                    letter_averages['F'] += 1
            
            letters = list(letter_averages.keys())
            averages = list(letter_averages.values())

            plt.plot(letters, averages, color = 'm', marker = '.')
            plt.title('Report of Section 1 Grades', fontsize = 20)
            plt.xlabel('Letter Grades', fontsize = 14)
            plt.ylabel('Number of Students', fontsize = 14)
            plt.ylim([0, 10.5])
            plt.yticks(range(0, 11, 1))
            plt.savefig('Report of Section 1 Grade Averages.png')
            plt.close()
        
        elif menu_choice == '4':
            print('\nYou Have Chosen Option 4 to Create a File of Your Class\' Average Grades.')
            new_student_gradebook = student_gradebook[:]
            new_student_gradebook.insert(6, 'Average Grade', cal_ave2())
            new_student_gradebook.drop([col for col in new_student_gradebook if col.startswith('Exam')], axis = 1, inplace = True)
            
            file_name = 'Section1Results.txt'
            
            f = open(file_name, 'w')
            for i in range(len(new_student_gradebook)):
                student_line_info = []
                
                last_name = new_student_gradebook.loc[i, 'Last Name']
                student_line_info.append(last_name)
                
                first_name = new_student_gradebook.loc[i, 'First Name']
                student_line_info.append(first_name)
                
                student_avg = new_student_gradebook.loc[i, 'Average Grade']
                student_line_info.append(str(student_avg))
                
                student_line = ','.join(student_line_info)
                
                f.write(f'{student_line}\n')

            f.close()
            print(f'Output File {file_name} Now Created in Directory')
            
        elif menu_choice == '5':
            print('\nYou Have Chosen Option 5 to Close this Program.')
            print('This Program Will Now Close. Thank You for Opening and Using This Program.')
            print('\nGoodbye.')
            print('\nCreated by Pete Challenger.')
            stop_program = True
        
        else:
            raise ValueError('Invalid Input.')
    
    except ValueError as excpt:
        print(f'\n{excpt}')
        print('You Either Entered an Invalid Number or You Entered a Word or Character Instead.')
        print('Please Try Again.')

