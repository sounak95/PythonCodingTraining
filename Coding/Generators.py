def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

def topten1():
    val=1
    while val<=10:
        yield val
        val+=1

values=topten1()

for i in values:
    print(i)

