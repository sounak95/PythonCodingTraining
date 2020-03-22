a=[{"name":'a', "rank":4},
   {"name":'b', "rank":2},
   {"name": 'b', "rank": 1}
   ]
print sorted(a,key=lambda x:x['rank'])

# class String:
#     def __init__(self,string):
#         self.string=string
#
#     def __repr__(self):
#         return 'Object: {}'.format(self.string)
#
#     def __add__(self, other):
#         return self.string+ other
#
# if __name__=='__main__':
#     string1=String('Hello')
#     print (string1+' Geeks')

# global i
# i=0
#
# def count():
#     global i
#     i+=1
#     print str(i)
#
# def func(f):
#     def inner():
#         return f()
#     return inner
#
# f=func(count)
# f()
# f()
# f()


# import os
#
# path = 'D:\\BDD_Cucumber\\BDD_POC'
#
# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     # for file in f:
#         # if '.txt' in file:
#         print "r: {}".format(r)
#         print "d: {}".format(d)
#         print "f: {}".format(f)
#
#         # files.append(os.path.join(r, file))
# print "*******************"
# for f in files:
#     print(f)

class Topten:
    def __init__(self):
        self.value =0
    def __iter__(self):
        return self
    def next(self):
        if self.value<10:
            n=self.value
            self.value+=1
            return n
        else:
            StopIteration

a=Topten()

# print(next(a))
# print(next(a))
# print(next(a))

# for item in a :
#     print item

# def topten1():
#     num=1
#     if num<10:
#         sq=num**2
#         yield sq
#         num+=1
# values = topten1()
# print next(values)
# print next(values)
# print next(values)
# print next(values)
# for i in values:
#     print i




