'''Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
'''

#L = [[1,3],[2,6],[7,9],[10,13],[15,18]]
L = [[1, 3], [4, 9], [8, 13], [12, 15], [20, 22], [23, 31], [24, 32], [40, 50]]
#L = [(1, 3), (4, 9), (8, 13), (12, 15), (20, 22), (23, 31), (24, 32), (40, 50)]
L = sorted(L)
print(L)

i = 1
print(len(L))
while i < len(L):

    if L[i][0] <= L[i-1][1]:
        L[i-1][1] = L[i][1]
        del L[i]
    else:
        i +=1
    #print("length of list is {}".format(len(L)))

print(L)