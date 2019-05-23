#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:04:21 2019

@author: Mr.Car
"""

def menu():
	a = '''
        +-------StudentManagementSystem----------+
        +----------------------------------------+
        | 1. add students grade information      |
        | 2. display everyone's grades           |
        | 3. index by stduent ID or names        |
        | 4. display one of the courses          |
        | 5. add course and grades               |
        | 6. clear information                   |
        |                               By Mr.Car|
        +----------------------------------------+
        '''
	print(a)

def newTitle():  # new grades title
	title = []
	while True:
		t = input('Please input a new Course q to quite:  ')
		if t == 'q':
			break
		else:
			title.append(t)
	print('Course adding is completed')
	return title


def addinfo():  # add grades information Function1&6
	info = {}
	if len(studentsInfo) == 0:
		info['StudentID+Name'] = []
	if 'StudentID+Name' in studentsInfo.keys():
		All_title = studentsInfo['StudentID+Name']
		info['StudentID+Name'] = All_title
	else:
		All_title = []
	All_title = All_title + newTitle()
	info['StudentID+Name'] = All_title
	while True:
		print(info['StudentID+Name'])
		k = input('please input StudentID+Name.(q to exit) eg:123XiaoHong :  ')
		if k == 'q':
			break
		v = input('please add grades in order eg: 99,88,60... :  ')
		vlist = list(map(float, v.split(",")))
		info[k] = vlist  # infor dictionary:ID-Name are keys,grades are values
	print(info)

	return info


def addNewStudents():
	info = {}
	while True:
		k = input('please input StudentID+Name.(q to exit)) eg:123XiaoLan :  ')
		if k == 'q':
			break
		if k in studentsInfo.keys():
			print('%s is in database. No need to add' % k)
		else:
			v = input('please add grades in order eg: 99,88,60... :  ')
			vlist = list(map(float, v.split(",")))
			info[k] = vlist
		return info


def stuInfo_everage(alist):  # compute everage of a student's grades
	alist
	if isinstance(alist[0], str):
		alist.append('Everage')
	else:
		l = sum(alist) / len(alist)
		alist.append(l)
	return alist


def showAllGrades(Info):  # display grades and average grades of all students Function2
	for key in Info:
		stuInfo_everage(Info[key])
	print('StudentID+Name', Info['StudentID+Name'])

	for key in Info:
		if key != 'StudentID+Name':
			print(key, Info[key])



def OneStudent():  # search students grades by ID or Name Function3
	isntexit = True
	k = input('Please input studentID or Name to index :  ')
	print('StudentID+Name', studentsInfo['StudentID+Name'])
	for key in studentsInfo:
		if k in key:
			print(key, studentsInfo[key])
			isntexit = False
	if isntexit:
		print('There is no such a student in database')
	return


def OneCourse():  # search grades by Courses Function4
	course = input('Please input the course that you want to check:  ')
	if course in studentsInfo['StudentID+Name']:
		num = studentsInfo['StudentID+Name'].index(course)
		print('StudentID+Name', course)
		i = 0
		j = 0
		for key in studentsInfo:
			if key != 'StudentID+Name':
				print(key, studentsInfo[key][num])
				j += 1.0
				i += studentsInfo[key][num]
		print('Everage of Grades', i / j)
	else:
		print('There is no such course in database')
	return


def addCourseAndGrades():
	# add title
	title = studentsInfo['StudentID+Name']
	title = title + newTitle()
	studentsInfo['StudentID+Name'] = title
	# add grades
	while True:
		k = input('please input StudentID+Name.(q to exit)) eg:123XiaoHei :  ')
		if k == 'q':
			break
		if k in studentsInfo.keys():
			v = input('please input new course grades of %s. eg:99,98...:  ' % k)
			vlist = map(float, v.split(","))
			studentsInfo[k] = studentsInfo[k] + vlist
		else:
			print(studentsInfo['StudentID+Name'])
			v = input('please input all grades of the new student %s. eg:99,98,97,...:  ' % k)
			vlist = map(float, v.split(","))
			studentsInfo[k] = vlist


def clearInfo():
	while True:
		op = input(
			'''
			+-------StudentManagementSystem----------+
			+----------------------------------------+
			| 0. clear all database                  |
			| 1. clear information of students       |
			| 2. remove course information           |
			|                               By Mr.Car|    
			+----------------------------------------+
			type num of function and execute
			type 'q' to exit              
			''')
		if op == 'q':
			break
		if op == '0':
			studentsInfo.clear()
		if op == '1':
			k = input('type ID or Name to find students')
			klist = []
			for key in studentsInfo:
				if k in key:
					klist.append(key)
			print(klist)
			if input('Do you want to remove them all (y/n):  ') == 'y':
				for i in klist:
					del studentsInfo[i]


global studentsInfo
studentsInfo = {}
while True:
	if len(studentsInfo) == 0 or studentsInfo['StudentID+Name'] == []:
		print(
		'''
        +-------StudentManagementSystem----------+
        +----------------------------------------+              
        | * There is nothing in database         |
        |   You must add information             |
        |                                        |
        | * Type 'q' to exit                     |
        |   Type any key to continue             |
        |                                        |        
        | * Type 'data'                          |
        |   input information from data.txt      |
        |                               By Mr.Car|
        +----------------------------------------+
              ''')
		if input() == 'q':
			break
		if input() == 'data':
			FromData()
		studentsInfo.update(addinfo())
		input()
	if studentsInfo['StudentID+Name'] != []:
		menu()
		op = input('please choose functions, type the number(q to quite):  ')
		if op == '1':
			print(studentsInfo['StudentID+Name'])
			studentsInfo.update(addNewStudents())
			input()
		if op == '2':
			import copy
			Info = copy.deepcopy(studentsInfo)
			showAllGrades(Info)
			input()
		if op == '3':
			OneStudent()
			input()
		if op == '4':
			OneCourse()
			input()
		if op == '5':
			addCourseAndGrades()
		if op == '6':
			clearInfo()
		if op == 'q':
			break