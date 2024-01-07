## numbers from the honeycombs

a = [1,3,5,4,2,6]
b = [1,2,5,6,3,4]
c = [1,4,2,3,5,6]
d = [1,5,3,2,6,4]
e = [1,2,3,4,5,6]
f = [1,6,5,4,3,2]
g = [1,3,5,2,4,6]

combs = [a,b,c,d,e,f,g]

## functions

def checkIndicesNextToEachOther(i1: int, i2: int):
    """check if i1 and i2 are numbers that are next to each other"""
    return abs(i1 - i2) == 1

def getSingleSideMatch(static1: list[int], matchIndex: int, comb: list[int]):
    """get match between static1 and comb at matchIndex of static1"""
    for i in range(len(comb)):
        if comb[i] == static1[matchIndex]:
            return (matchIndex, i)

def getDoubleSideMatch(static1: list[int], static2: list[int], m1: tuple[int, int], comb: list[int], goUpOnS1: bool):
    """get match between static1, static2 and comb with m1 being the match between static1 and static2; goUpOnS1 is whether to increment the index on static1"""
    if goUpOnS1:
        #get match between static1 and comb
        s1c = getSingleSideMatch(static1, (m1[0] + 1) % len(static1), comb)
        #get match between static2 and comb
        s2c = getSingleSideMatch(static2, (m1[1] - 1) % len(static2), comb)
        #check if the indices are next to each other in comb
        if checkIndicesNextToEachOther(s1c[1], s2c[1]):
            return (m1, s1c, s2c)
    else:
        #do the same thing but on the opposite sides of static1 and static2
        s1c = getSingleSideMatch(static1, (m1[0] - 1) % len(static1), comb)
        s2c = getSingleSideMatch(static2, (m1[1] + 1) % len(static2), comb)
        if checkIndicesNextToEachOther(s1c[1], s2c[1]):
            return (m1, s1c, s2c)
    return None

def getTripleSideMatch(static1, static2, static3, m1, m2, comb):
    """get match between static1, static2, static3 and comb with m1 and m2 being the matche between static1 and static2"""
    #get match between static1, static2 and comb
    s1s2c = getDoubleSideMatch(static1, static2, m1, comb, False)
    if s1s2c is not None:
        #get match between static3 and comb
        s3c = getSingleSideMatch(static3, (s1s2c[2][1] + 1) % len(static3), comb)
        #check if the indices are next to each other in comb
        if checkIndicesNextToEachOther(s1s2c[2][1], s3c[1]):
            return (m1, m2, s1s2c[1], s1s2c[2], s3c)
    return None


## tests
if __name__ == "__main__":
    print(getSingleSideMatch(a, 0, b))
    print(getDoubleSideMatch(a, b, (0,0), e, True))
    print(getTripleSideMatch(c, a, b, (2,4), (0,0), d))
