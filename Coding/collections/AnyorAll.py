# https://www.hackerrank.com/challenges/any-or-all/problem
def is_pal(n):
    S=str(n)
    return all([s==t for s,t in zip(S,reversed(S))])

def meets_conditions(L):
    if not all([l>0 for l in L]):
        return False
    return bool(any([is_pal(l) for l in L]))

N=int(raw_input())
L=map(int, raw_input().split())
print meets_conditions(L)