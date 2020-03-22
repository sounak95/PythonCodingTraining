list1=[1,2,"3",4,"5"]
list2=[4,"5",6,7,"8"]

def list_difference(list1,list2):
    return set(list1).symmetric_difference(set(list2))

print(list_difference(list1,list2))

print(set((set(list1)-set(list2))).union(set(list2)-set(list1)))
