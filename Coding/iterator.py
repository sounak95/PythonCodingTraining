class TopTen:
    def __init__(self):
        self.val=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.val<=10:
            # print(self.val)
            num = self.val
            self.val += 1
            return num


        else:
            raise StopIteration




if __name__=="__main__":
    values=TopTen()
    for i in values:
        print(i)

