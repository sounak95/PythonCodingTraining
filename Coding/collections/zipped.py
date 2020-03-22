N, X = map(int, raw_input().split())
list_of_marks = []
for subject in xrange(X):
    list_of_marks += [map(float,raw_input().split())]

print zip(*list_of_marks)
for student_marks in zip(*list_of_marks):
    print student_marks
    print sum(student_marks)/X