import sys
arr = []

#arr.append(','.join(input().split()))

#for i in input().split():
#    arr.append(','.join(int(i)))

#for i in input():
#    arr.append(int(i))
#print(arr)


'''
for i in input():
    arr.append(int(i))

even_list = [num for num in arr if num%2 == 0]
print(even_list)

'''

'''
def isprime(num,n=2):
    if (num == 2):
        return True
    if n*n > num:
        return True
    elif num%n == 0:
        return False
    else:
        return isprime(num,n+1)

def lessPrime(n):
    for i in range (n-1,2,-1):
        if isprime(i) is True:
            return i
'''
'''
#min steps required to make n to 1
#If n is divisible by 2 then we may reduce n to n/2.
#If n is divisible by 3 then you may reduce n to n/3.
#Decrement n by 1.
def minsteps(k):
    count = 0

    while k > 1:
        if k%3 ==0:
            k = k//3
            count += 1
        elif (k-1)%3 == 0:
            k = k-1
            count +=1
            continue
        elif k%2 ==0:
            k = k//2
            count += 1
        else:
            k = k-1
            count +=1

    print(count)

import pdb
#pdb.set_trace()
minsteps(6)


arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]

import pdb
pdb.set_trace()


def minJumps(arr, k):
    # jumps[0] will hold the result
    jumps = [0 for i in range(k)]

    # Minimum number of jumps needed
    # to reach last element from
    # last elements itself is always 0
    # jumps[n-1] is also initialized to 0

    # Start from the second element,
    # move from right to left and
    # construct the jumps[] array where
    # jumps[i] represents minimum number
    # of jumps needed to reach arr[m-1]
    # form arr[i]
    for i in range(k - 2, -1, -1):

        # If arr[i] is 0 then arr[n-1]
        # can't be reached from here
        if (arr[i] == 0):
            jumps[i] = float('inf')

            # If we can directly reach to
        # the end point from here then
        # jumps[i] is 1
        elif (arr[i] >= k - i - 1):
            jumps[i] = 1

        # Otherwise, to find out the
        # minimum number of jumps
        # needed to reach arr[n-1],
        # check all the points
        # reachable from here and
        # jumps[] value for those points
        else:
            # initialize min value
            min1 = float('inf')

            # following loop checks with
            # all reachable points and
            # takes the minimum
            for e in range(i + 1, k):
                if (e <= arr[i] + i):
                    if (min1 > jumps[e]):
                        min1 = jumps[e]


            # Handle overflow
            if (min1 != float('inf')):
                jumps[i] = min1 + 1
            else:
                # or INT_MAX
                jumps[i] = min1

    return jumps[0]


print(minJumps(arr,len(arr)-1))



'''

lst = [1,2,3,4,5,6]
#print(lst[0:3])
import pdb
#pdb.set_trace()

def subs(arr):
    if arr == []:
        return [[]]

    x = subs(arr[1:])

    return x + [[arr[0]] + y for y in x]

#res = subs([1,2,3])
#print(res)

import pdb
#pdb.set_trace()

def sub2(arr):
    if arr == []:
        return [[]]

    x = sub2(arr[1:])

    return x + [[arr[0]] + y for y in x]

res = sub2([1,2,3])
print(res)

for i in res:
    if 