def compareTheTriplets(a,b):
    AliceScore=0
    BobScore=0
    for i in range(3):
        if a[i]>b[i]:
            AliceScore=AliceScore + 1
        elif b[i]>a[i]:
            BobScore = BobScore + 1
    return [AliceScore,BobScore]

a=[5,6,7]
b=[3,6,10]
print(compareTheTriplets(a,b))
