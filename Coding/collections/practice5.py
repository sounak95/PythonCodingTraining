#https://www.hackerrank.com/challenges/most-commons/problem
# str1 = "ccaabbbde"
# str1="qwertyuiopasdfghjklzxcvbnm"
# from collections import OrderedDict
# ord = OrderedDict()
# for item in str1:
#     if item in ord:
#         ord[item] +=1
#     else:
#         ord[item]=1
# # print ord.values()
#
# import operator
# sorted_x = sorted(ord.items(), key=operator.itemgetter(1), reverse=True)
# print sorted_x
# for key,value in sorted_x[:3]:
#     print "{} {}".format(key,value)


#https://www.hackerrank.com/challenges/most-commons/problem
S = "aabbbccde"
print ord('a')
letters = [0]*26

for letter in S:
    letters[ord(letter)-ord('a')] += 1
print letters
for _ in range(3):

    max_letter = max(letters)
    # print max_letter

    for index in range(26):
        if max_letter == letters[index]:
            print chr(ord('a')+index), max_letter
            letters[index] = -1
            break

