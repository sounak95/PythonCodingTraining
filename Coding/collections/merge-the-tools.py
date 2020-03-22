

def merge_the_tools(string, k):
    str1 = string
    chunk = int(len(str1) / k)
    # print len(str1)
    # print chunk
    for i in range(chunk):
        merge = ""
        for ch in str1[i*k:(i +1)*k]:
            if ch not in merge:
                merge += ch
        print merge

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)

