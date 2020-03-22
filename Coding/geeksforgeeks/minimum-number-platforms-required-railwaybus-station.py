#https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/


def findPlatform(arr,dep,n):
    i=1
    j=0
    plat_needed=1
    res=1
    arr.sort()
    dep.sort()

    while(i<n and j<n):
        if arr[i]<dep[j]:
            plat_needed+=1
            i+=1
            if plat_needed>res:
                res=plat_needed

        else:
            plat_needed-=1
            j+=1
        print ("plat_needed: {}".format(plat_needed))
    return res

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ",
findPlatform(arr, dep, n))

