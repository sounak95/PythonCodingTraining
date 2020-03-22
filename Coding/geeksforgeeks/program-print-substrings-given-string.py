#https://www.geeksforgeeks.org/program-print-substrings-given-string/

str1="forgeeksskeegfor"

count=0
max=float('-inf')
pal_str=""
for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        count+=1
        print(str1[i:j])
        str2=str1[i:j]
        if str2==str2[::-1] :
            if len(str2)>max:
                max=len(str2)
                pal_str=str2
            # print("Palindroms found: {}".format(str2))


print(pal_str)


