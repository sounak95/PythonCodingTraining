#
# def person_lister(f):
#     def fun(person):
#         # complete the function
#         return f(person)
#     return fun
#
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [raw_input().split() for i in range(int(raw_input()))]
#     # print '\n'.join(name_format(people))
#     for item in sorted(people,key=lambda x:x[2]):
#         print name_format(item)


def formal(ns):
    first,last,age,sex = ns
    return ('Mr. ' if sex == 'M' else 'Ms. ') + first + ' ' + last

def std(f):
    def inner(ns):
        return map(formal, f(ns))
    return inner

@std
def nsort(ns):
    return [x[1] for x in sorted(enumerate(ns), key=lambda x: (x[1][2],x[0]))]

n = int(raw_input())
for x in nsort([raw_input().split() for x in range(n)]):
    print x