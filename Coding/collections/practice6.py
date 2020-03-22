#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
s = int(raw_input())
result = []
for i in range(s) :
	result.append(raw_input())

result2 = []
for x in result :
	y = x[len(x)-10:]
	result2.append("+91 "+ y[0:5]+" "+y[5:10]);

result2.sort()
for x in result2 :
	print x