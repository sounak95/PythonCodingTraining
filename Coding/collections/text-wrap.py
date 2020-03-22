#https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    str1=string
    n=max_width
    str2=""
    for i in range(0,len(str1),n):
        str2+= str1[i:i+n] + "\n"
    return str2

if __name__ == '__main__':
    string, max_width = "bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd", 9
    result = wrap(string, max_width)
    print result

