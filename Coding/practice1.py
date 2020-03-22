#https://www.hackerrank.com/challenges/no-idea/problem
# n=3
# m=2
# list1=[1,5,3]
# A= [3,1]
# B=[5,7]
# happ_count=0
# for item in list1:
#     if item in A:
#         happ_count = happ_count +1
#     elif item in B:
#         happ_count = happ_count - 1
#     else:
#         pass
# print happ_count

m,n=tuple(map(int,raw_input().split()))
arr=list(map(int,raw_input().split()))
A=set(map(int,raw_input().split()))
B=set(map(int,raw_input().split()))
happy=len([x for x in arr if x in A])
sad=len([i for i in arr if i in B])
print happy-sad

# a = raw_input().split()
# print a