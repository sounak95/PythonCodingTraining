def count_substring(string, sub_string):
    str1 = string
    str2 = sub_string
    m = len(str1)
    n = len(str2)

    count =0
    for i in range(m - n +1):
        if str1[i:i + n] == str2:
            count+=1
    return count
if __name__ == '__main__':
    # string = raw_input().strip()
    # sub_string = raw_input().strip()

    count = count_substring("ABCDCDC", "CDC")
    print count