#https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Regular-Expressions

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# print('\tTab')
#
pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
#
# pattern = re.compile(r'\.')
#
# matches = pattern.finditer(text_to_search)f
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'coreyms\.com')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'coreyms\.com')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'\bHa')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'\BHa')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)
#
# pattern = re.compile(r'^Start')
# matches = pattern.finditer(sentence)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'\d\d\d[.-]\d\d\d[-.]\d\d\d\d')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'[89]00[.-]\d\d\d[-.]\d\d\d\d')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'[1-5]')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'[a-zA-Z]')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'[^a-zA-Z]')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'[^b]at')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'Mr\.?')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# emails = '''
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafer@my-work.net
# '''
#
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|net|edu)')
#
# matches = pattern.finditer(emails)
#
# for match in matches:
#     print(match)

# str1="amnnn"
#
# pattern = re.compile(r'[amn]?')
#
# matches = pattern.finditer(str1)
#
# for match in matches:
#     print(match)

# import os
# dirpath = os.getcwd()
# cur_dir=dirpath + "\\"
# print(cur_dir)