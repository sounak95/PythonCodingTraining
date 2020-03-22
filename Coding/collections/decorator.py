def wrapper(f):
    def fun(l):
        # complete the function
        l1=[]
        for item in l:
            l1.append("+91 " + item[-10:-5] + " " + item[-5:])
        return f(l1)
    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)