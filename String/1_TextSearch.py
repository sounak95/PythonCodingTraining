"""
check-string-substring-another


"""
def search(txt,pat):
    n=len(txt)
    m=len(pat)
    for i in range(n-m):
        for j in range(m):
            if(txt[i+j]!=pat[j]):
                break
        if(j==m-1):
            print("patter {} found at {}".format(pat,i))

txt = "geeksforgeeks"
pat = "for"
search(txt,pat)