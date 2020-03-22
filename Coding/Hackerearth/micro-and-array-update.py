#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/

n_testCase=int(input())
for _ in range(n_testCase):
    n_size, max_val =map(int, raw_input().split())
    l1=map(int, raw_input().split())
    print max_val-min(l1)

