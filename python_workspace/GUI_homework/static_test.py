class Count:
    staticCount=0

    def __init__(self, count):
        self.count = count




c1=Count(0)
c2=Count(0)
Count.staticCount = Count.staticCount+1
Count.staticCount = Count.staticCount+1
print("c1.staticCount = " , c1.staticCount, "c2.staticCount=",c2.staticCount)
c1.count = c1.count+1
c2.count = c2.count+1
print("c1.count = ",c1.count, "c2:count =",c2.count)



