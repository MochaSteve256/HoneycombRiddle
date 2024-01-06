a = [1,3,5,4,2,6]
b = [1,2,5,6,3,4]
c = [1,4,2,3,5,6]
d = [1,5,3,2,6,4]
e = [1,2,3,4,5,6]
f = [1,6,5,4,3,2]
g = [1,3,5,2,4,6]

waben = [a,b,c,d,e,f,g]

def getSingeSideMatch(static1, waben):
    pass

def getDoubleSideMatch(static1, static2, m1, waben):
    pass

def getTripleSideMatch(static1, static2, static3, m1, m2, waben):
    pass


for wabe in waben:
    #get each wabe index that matches wabe[0]
    wabenOhneSelbst = waben.copy()
    wabenOhneSelbst.remove(wabe)
    for andereWabe in wabenOhneSelbst:
        #do stuff
        pass