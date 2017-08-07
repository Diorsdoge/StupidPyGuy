# -- coding: utf-8 --

import os
import random


studentFile = open('student')
masterFile = open('master')
student = {}
master = {}
sFull = {}
while True:
	line = studentFile.readline()
	if not line:
		break
	student[line] = int(0)

# print student

while True:
	line = masterFile.readline()
	if not line:
		break
	master[line.split(':')[0]] = line.split(':')[1]
	sFull[line.split(':')[0]] = 0

group = len(master)
# print master
print sFull

for stu in student:
	while True:
		n = random.randint(1,5)
		if sFull[str(n)] <= int(master[str(n)]):
			stu[0] = n
			sFull[n] += 1
			break

studentFile.close()
masterFile.close()
print student
	









