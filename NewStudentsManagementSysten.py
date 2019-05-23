#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pandas as pd

class StuInfo():
	def __init__(self):
		if input('输入‘y’从文件中读取学生数据,‘q’取消:') == 'y':
			self.info = pd.read_csv('1.csv', encoding='GB2312')
			self.info['学号'] = self.info['学号'].astype('str')
			print(self.info)
		else:
			self.info = pd.DataFrame()
	def menu(self):
		print(
			'''
			Function list
			==================================
			*：从文件中导入信息：1.csv
			0：退出程序
			1：添加新的学生信息：学号和姓名
			2：添加新的课程信息：课程名称
			3：添加学生成绩：整数
			4：删除学生信息
			5：删除课程信息
			6：修改学生信息：课程成绩
			7：查询显示学生信息
			8：统计课程信息
			'''
		)
	def add_new_stu(self):
		#添加新的学生信息：学号和姓名
		ind = input('请输入学号：')
		nam = input('请输入姓名：')
		temp_dict = {'学号':[ind],'姓名':[nam]}
		temp = pd.DataFrame(temp_dict)
		self.info = self.info.append(temp,sort=False,ignore_index=True)
	def add_new_course(self):
		#添加新的课程信息
		new_course = input('请输入新的课程名称：')
		self.info[new_course] = ['未添加']*len(self.info)
	def add_new_grade(self):
		#添加学生成绩
		stu_ind = input('请输入学号：')
		stu_course = input('请输入课程名称：')
		stu_grade = input('请输入学生成绩：')
		ind = self.info[self.info['学号'] == stu_ind].index
		self.info.loc[ind,stu_course] = int(stu_grade)
	def remove_student(self):
		#将学生信息删除
		stu_ind = input('请输入要删除的学生学号：')
		ind = self.info[self.info['学号'] == stu_ind].index
		print(list(ind))
		self.info.drop(index=ind,inplace=True)
	def remove_course(self):
		#将课程信息删除
		stu_course = input('请输入要删除的课程名称：')
		self.info.drop([stu_course],axis=1,inplace=True)
	def modify(self):
		stu_ind = input('请输入要修改学生的学号或姓名：')
		stu_course = input('请输入课程名称：')
		stu_grade = input('请输入要修改学生成绩：')
		try:
			int(stu_ind)
			str(stu_ind)
			ind = self.info[self.info['学号'] == stu_ind].index
		except:
			ind = self.info[self.info['姓名'] == stu_ind].index
		self.info.loc[ind,stu_course] = int(stu_grade)
	def show(self):
		print(self.info)
	def analyse(self):
		#统计显示课程信息
		print(self.info.iloc[:,2:].describe())
	def student_info(self):
		#统计某学生课程信息
		stu_ind = input('请输入要查询的学生的学号或姓名：')
		try:
			int(stu_ind)
			str(stu_ind)
			ind = self.info[self.info['学号'] == stu_ind].index
		except:
			ind = self.info[self.info['姓名'] == stu_ind].index
		temp = self.info.iloc[ind,:]
		temp_1 = self.info.iloc[ind,2:]
		s = 0
		for i in range(len(list(temp_1))):
			s = s + temp_1.iloc[:,i]
		eve = s/len(list(temp_1))
		print(temp,'平均成绩:%.2f'%eve)

# stu=StuInfo()
# while True:
# 	stu.menu()
# 	flag = input('请输入功能序号：')
# 	if flag =='0':
# 		break
# 	if flag =='1':
# 		while True:
# 			if input('任意键继续，\'q\'退出：') == 'q':
# 				break
# 			stu.add_new_stu()
# 		stu.show()
# 	if flag =='2':
# 		stu.add_new_course()
# 		stu.show()
# 	if flag == '3':
# 		stu.add_new_grade()
# 		stu.show()
# 	if flag=='4':
# 		stu.remove_student()
# 		stu.show()
# 	if flag == '5':
# 		stu.remove_course()
# 		stu.show()
# 	if flag == '6':
# 		stu.modify()
# 		stu.show()
# 	if flag == '7':
# 		stu.student_info()
# 	if flag == '8':
# 		stu.analyse()

import tkinter as tk
# 创建一个主窗口，用于容纳整个GUI程序
root = tk.Tk()
# 设置主窗口对象的标题栏
root.title("学生成绩信息管理系统——Mr.Car")
root.geometry('1000x600')
# 添加一个Label组件，Label组件是GUI程序中最常用的组件之一
# Label组件可以显示文本、图标或者图片
# 在这里我们让他们显示指定文本
theLabel = tk.Label(root, text="学生成绩信息管理系统——Mr.Car")
b = tk.Button(root, text="从文件中导入学生成绩", command='')
# 然后调用Label组建的pack()方法，用于自动调节组件自身的尺寸
theLabel.pack()
b.pack()
# 注意，这时候窗口还是不会显示的...
# 除非执行下面的这条代码！！！！！
root.mainloop()