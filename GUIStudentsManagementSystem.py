#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
#中文导致不能对齐，这两行也太厉害了，可以将df对齐。
class StuInfo():
	def __init__(self):
		self.info = pd.DataFrame()
		self.menu = '''
			Function list
			==================================
			*：从文件中导入信息：1.csv
			1：添加新的学生信息：学号和姓名
			2：添加新的课程信息：课程名称
			3：添加学生成绩：整数
			4：删除学生信息
			5：删除课程信息
			6：修改学生信息：课程成绩
			7：查询显示学生信息
			8：统计课程信息
			'''

	def add_new_stu(self, ind, nam):
		#添加新的学生信息：学号和姓名
		ind = str(ind)
		nam = str(nam)
		temp_dict = {'学号':[ind],'姓名':[nam]}
		temp = pd.DataFrame(temp_dict)
		self.info = self.info.append(temp,sort=False,ignore_index=True)
		return self.info
	def add_new_course(self,new_course):
		#添加新的课程信息
		new_course = str(new_course)
		self.info[new_course] = [0]*len(self.info)
		return self.info
	def add_new_grade(self,stu_ind,stu_course,stu_grade):
		#添加学生成绩
		stu_ind = str(stu_ind)
		stu_course = str(stu_course)
		stu_grade = str(stu_grade)
		ind = self.info[self.info['学号'] == stu_ind].index
		self.info.loc[ind,stu_course] = int(stu_grade)
		return self.info
	def remove_student(self,stu_ind):
		#将学生信息删除
		stu_ind = str(stu_ind)
		ind = self.info[self.info['学号'] == stu_ind].index
		print(list(ind))
		self.info.drop(index=ind,inplace=True)
		return self.info
	def remove_course(self,stu_course):
		#将课程信息删除
		stu_course = str(stu_course)
		self.info.drop([stu_course],axis=1,inplace=True)
		return self.info
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
		return self.info
	def analyse(self):
		#统计显示课程信息
		return self.info.iloc[:,2:].describe()
	def student_info(self,stu_ind):
		#统计某学生课程信息
		stu_ind = str(stu_ind)
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
		return temp,'平均成绩:%.2f'%eve


import tkinter as tk
root = tk.Tk()
root.title("学生成绩信息管理系统——Mr.Car")
frm = tk.Frame(root)
frm.pack()

frm_l = tk.Frame(frm)
frm_l.pack(side='left')

frm_r = tk.Frame(frm)
frm_r.pack(side='right')

stu=StuInfo()


def menu():
	t_1.delete('1.0','end')
	t_1.insert('insert',stu.menu)


b_0 = tk.Button(frm_l,text='功能目录',command=menu)
b_0.pack(fill=tk.X, expand=1)


def pdread():
	t_1.delete('1.0','end')
	stu.info = pd.read_csv('1.csv', encoding='GB2312')
	stu.info['学号'] = stu.info['学号'].astype('str')
	t_1.insert('insert',stu.info)


b_1 = tk.Button(frm_l, text="从文件中导入学生成绩",command=pdread)
b_1.pack(fill=tk.X, expand=1)

def f1():
	t_1.delete('1.0', 'end')
	ind = e_1.get()
	nam = e_2.get()
	if len(ind) != 0 and len(nam) !=0:
		a = stu.add_new_stu(ind, nam)
		t_1.insert('insert', a)
	else:
		t_1.insert('insert','输入错误请重试')


b_2 = tk.Button(frm_l,text='添加学生信息：学号与姓名',command=f1)
b_2.pack(fill=tk.X, expand=1)


def f2():
	t_1.delete('1.0', 'end')
	new_course = e_3.get()
	if len(new_course) != 0:
		a = stu.add_new_course(new_course)
		t_1.insert('insert', a)
	else:
		t_1.insert('insert','输入错误请重试')


b_3 = tk.Button(frm_l,text='添加课程信息：课程名称',command=f2)
b_3.pack(fill=tk.X, expand=1)


def f3():
	t_1.delete('1.0', 'end')
	stu_ind = e_1.get()
	stu_course = e_3.get()
	stu_grade = e_4.get()
	if len(stu_ind) != 0 and len(stu_course) != 0 and len(stu_grade) != 0:
		a = stu.add_new_grade(stu_ind,stu_course,stu_grade)
		t_1.insert('insert', a)
	else:
		t_1.insert('insert','输入错误请重试')


b_4 = tk.Button(frm_l,text='添加已有学生成绩：学号，课程，成绩',command=f3)
b_4.pack(fill=tk.X, expand=1)


def f4():
	t_1.delete('1.0', 'end')
	stu_ind = e_1.get()
	if len(stu_ind) != 0:
		a = stu.remove_student(stu_ind)
		t_1.insert('insert', a)
	else:
		t_1.insert('insert','输入错误请重试')


b_5 = tk.Button(frm_l,text='删除已有学生信息',command=f4)
b_5.pack(fill=tk.X, expand=1)

def f5():
	t_1.delete('1.0', 'end')
	stu_course = e_3.get()
	if len(stu_course) != 0:
		a = stu.remove_course(stu_course)
		t_1.insert('insert', a)
	else:
		t_1.insert('insert','输入错误请重试')


b_6 = tk.Button(frm_l,text='删除已有课程信息',command=f5)
b_6.pack(fill=tk.X, expand=1)

b_7 = tk.Button(frm_l,text='修改已有学生成绩：学号，课程，成绩',command=f3)
b_7.pack(fill=tk.X, expand=1)


def f6():
	t_1.delete('1.0', 'end')
	try:
		if len(e_1.get()) != 0 :
			stu_ind = e_1.get()
		else:
			stu_ind = e_2.get()
		if len(stu_ind) != 0:
			(a,b) = stu.student_info(stu_ind)
			t_1.insert('insert', a)
			t_1.insert('insert', b )
		else:
			t_1.insert('insert','输入错误请重试')
	except:
		t_1.insert('insert','输入错误请重试')

b_8 = tk.Button(frm_l,text='根据学号或姓名查找学生信息',command=f6)
b_8.pack(fill=tk.X, expand=1)


def f8():
	t_1.delete('1.0', 'end')
	try:
		a = stu.analyse()
		t_1.insert('insert',a)
	except:
		t_1.insert('insert','系统中还没有成绩！！！')


b_9 = tk.Button(frm_l,text="各科成绩分析",command=f8)
b_9.pack(fill=tk.X, expand=1)


def f9():
	t_1.delete('1.0', 'end')
	try:
		a = stu.show()
		t_1.insert('insert',a)
	except:
		t_1.insert('insert','系统中还没有成绩！！！')


b_10 = tk.Button(frm_l,text="显示成绩单",command=f9)
b_10.pack(fill=tk.X, expand=1)


l_0 = tk.Label(frm_l,text='').pack()
frm_ll = tk.Frame(frm_l)
frm_ll.pack(side='left')
frm_lr = tk.Frame(frm_l)
frm_lr.pack(side='right')

l_1 = tk.Label(frm_ll,text='学号：').pack()
e_1 = tk.Entry(frm_lr)
e_1.pack(fill=tk.X, expand=1)

l_2 = tk.Label(frm_ll,text='姓名：').pack()
e_2 = tk.Entry(frm_lr)
e_2.pack(fill=tk.X, expand=1)

l_3 = tk.Label(frm_ll,text='课程：').pack()
e_3 = tk.Entry(frm_lr)
e_3.pack(fill=tk.X, expand=1)

l_4 = tk.Label(frm_ll,text='成绩：').pack()
e_4 = tk.Entry(frm_lr)
e_4.pack(fill=tk.X, expand=1)

t_1 = tk.Text(frm_r,width=75,height=35)
a='''
                            l""tznwabXJW08WW8WWL////////(/////////////11///
                          ////////////////#///&Y#})//{\{//|////)//////B@///
                      ///////////////////////Z1QJY0%/\(}Z//1//////////$////
                    /////////////////////////////\h##J/W#B&X/////////\Q8///
                  d/////////////////////////////////O*X*XXL8Q1|/M@/////%///
                 J////////////////////////////////////hwbmb*LZ@/8//\//\||//
                 x//////////////////////////////////////a*aowXb/BMW%/1/\///
                 Wz/}////////////////////$///////////////m>[+rjcdqhaodwqLqY
                n   Z%k//////)////bk//JJo/M/}///////////_             ' '^i
                  c'+&$////Jw%///t;//d:"0kkxd/@/////////x       ' ,:i>?_+cu
                 ?zfp////%c  'pqmx//ww mx]"aq/////////@m           l ;~ixft
                 Qb///// o`  /////Ln. -j]zx%!kJhq////M"'            ` ^<[nv
            vk ////@///k+       +t  n/rn/r#//j/|/w               ';f-fccwuq
           v]//////////>               fkp:  .lc>"/                  l++?-t
         im////////////!                h^     r//k               ,"!I<ffxk
         p/////////////u               p      /////             ,'``ll+r-tt
        dL/////  j//////c      /.     r-    /////W                   ,>[jfr
         q//    //////////         aXOb`  ///////h             ,      ,"-x-
         /    n///////Q/.^ ,?           a////////k^          '`Ii" '>-t-tnt
       j     /////       .   ^          lk[i;+/.[ vnd+         ;fti+vqcqbda
          .//      ^//d                  +h ]             vu   `i+uvnzmbaho
    Yji^`w      //////x .                ,h                    npmphmapcdvk
.   mopct!   ///////// /Il;"_                                   .qdmpmbmd*X
    kq   //  /////////    ~^"    .   d                            ,dwkqhJ%J
   <  _f//n  /////////        ./                                    jop*b0k
/.    j/< /q /k//////                                                 ,ZOO8
h    .> q/ ;  //////I                                                   +J&
        /   .f///////                                                    ~p
        /     ///b///c/                                                    
        /     ./o///                                                       
              | /b,\                                                       
                  //                                                       
                    t                                   !m                 
   ///                                                 ?                   
'                                                     <l                   
'''
t_1.insert('insert',a)
t_1.pack()

root.mainloop()