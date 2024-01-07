from functions import *

## algorithm
# approach:
# define a center comb
# define a side comb
# doubleMatch/tripleMatch all remaining combs until it fails
#   if it fails, cycle the remaining combs in the array, then try again
#   if all combinations since the last fail still fail, remove a piece from the static combs and cycle again, etc.
#   if all pieces execpt the side comb are removed and it still fails, cycle the side comb and do all the above steps again

for center in combs:
    remainingCombs = combs.copy()
    remainingCombs.remove(center)
    staticCombs = [center]
    matches = []
    for i in range(6):
        for sideComb in remainingCombs:
            staticCombs.append(sideComb)
            matches.append(getSingleSideMatch(center, i, sideComb))
            remainingCombs.remove(sideComb)
            for j in range(len(remainingCombs)):
                print(center, sideComb, matches[-1], remainingCombs[j])
                x = getDoubleSideMatch(center, sideComb, matches[-1], remainingCombs[j], True)
                if x is not None:
                    staticCombs.append(remainingCombs[j])
                    remainingCombs.remove(remainingCombs[j])
                    matches.append(x)