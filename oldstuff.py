for wabe in combs:
    #get each comb index that matches wabe[0]
    combsWithoutSelf = combs.copy()
    combsWithoutSelf.remove(wabe)
    for andereWabe in combsWithoutSelf:
        #do stuff
        pass