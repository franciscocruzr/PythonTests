# define a function for possible clock time with 4 entries for easier input
# complexity of O(n^4) with n = len(array)
# checks every possible combination and discards the ones that are not permutations
def possibleClockTimes(A, B, C, D):
    variableArray = [A,B,C,D]
    count = 0 #counts possible times
    for i in range(4):
        for j in range(4):
            if i == j: continue #check if they are the same to stop this nested loop when they are not a permutation
            for k in range(4):
                if k == j or k == i: continue #check if they are the same to stop this nested loop when they are not a permutation
                for l in range(4):
                    if l == k or l == i or l == j: continue #check if they are the same to stop this nested loop when they are not a permutation
                    if (10*variableArray[i] + variableArray[j]) < 24 and (10*variableArray[k] + variableArray[l]) < 60: # check if this permutation is a possible time
                        count += 1 # add to the count
                        print(str(variableArray[i])+str(variableArray[j])+":"+str(variableArray[k])+str(variableArray[l])) # print the possible time
    print("There are " + str(count) + " possible clock times")

possibleClockTimes(1,2,3,4)
