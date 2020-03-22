#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
from collections import namedtuple
nStudents = int(raw_input())
Student = namedtuple('Student', raw_input().split())
students = []
avg = 0;
for n in range(nStudents):
    students.append(Student(*raw_input().split()))

for s in students:
    avg += float(s.MARKS)
print '%0.2f' % (float(avg)/float(nStudents))
