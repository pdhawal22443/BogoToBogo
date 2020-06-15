#Check if two strings are anagrams
# o/p -
'''(('evil', 'vile'), True)
(('pat', 'tap'), True)
(('mile', 'nile'), False)'''

def isanagram(str1,str2):
    if (sorted(list(str1)) != sorted(list(str2))):
        return False
    else:
        return True

words = [("evil","vile"), ("pat","tap"),("mile","nile")]
for w in words:
    print(w , isanagram(w[0],w[1]))


#Group Anagrams together
lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = {}

def groupAnagram(lst):
    for i in lst:
        if ' '.join(sorted(list(i))) in res:
            res[' '.join(sorted(list(i)))].append(i)
        else:
            res[' '.join(sorted(list(i)))] = [i]

groupAnagram(lst)
print(res)

res1 = []
for key in res.keys():
    res1.append(res[key])

print(res1)

#====================================================
#Making Anagram , Two strings are given ,
#you can delete any characters from any two strings to make them Anagrams
#Return the min number of deletions are required
#https://www.hackerrank.com/challenges

#test1 = 'adbc'
#test2 = 'acbe'
test1 = 'aaaaab'
test2 = 'bbbbba'
count = 0

dict1 = dict((k,test2.count(k)) for k in test1)
dict2 = dict((k,test1.count(k)) for k in test2)

print(dict1)
print(dict2)

for key in dict1.keys():
    if dict1[key] == 0:
        count += 1
    else:
        if dict1[key] != dict2[key]:
            count += abs(dict1[key] - dict2[key])

for key2 in dict2.keys():
    if dict2[key2] == 0:
        count += 1

print("Mininum deletion required is {}".format(count))

#================================================================================
'''
Strings: Alternating Characters
We are given a string containing characters A and B only. Our task is
to change it into a string such that there are no matching adjacent characters.
To do this, we are allowed to delete zero or more characters in the string.

Our task is to find the minimum number of required deletions.
Ex - AAAAA - min 4 deletions required
    ABBAAA - min 3 deletions required
    ABABAB - Zero deletions required
'''

str1 = 'AAAAAAAA'
print(len([i for i in range(len(str1) - 1) if str1[i] == str1[i+1]]))

#=================================================================================
'''String with the same frequency of characters
We considers a string to be valid if all characters of the string appear
the same number of times. It is also valid if he can remove just 1 character
at 1 index in the string, and the remaining characters will occur the same
number of times. Given a string s, determine if it is valid. If so, return True,
otherwise return False.
Problem source - https://www.hackerrank.com/challenges

'''

#==============================================================================
#common elements of two lists
list1 = [1,3,5,7]
list2 = [3,5,8,9]

print([i for i in list1 if i in list2])

#==============================================================================
'''String with the same frequency of characters
We considers a string to be valid if all characters of the string appear the same
 number of times. It is also valid if he can remove just 1 character at 1
  index in the string, and the remaining characters will occur the same 
  number of times. Given a string s, determine if it is valid. If so,
   return True, otherwise return False.
   ex :
   abc - {'a': 1, 'b': 1, 'c': 1}  True

    abcc - {'a': 1, 'b': 1, 'c': 2}  True

    aabbcd - {'a': 2, 'b': 2, 'c': 1, 'd': 1}  False
   '''

str11 = 'aaabb'

def isvalidString(str):
    dict14 = dict((k,str11.count(k)) for k in str11)
    print(dict14)
    maximum = max(list(dict14.values()))
    minimum = min(list(dict14.values()))
    print("max is {}".format(maximum))
    print("min is {}".format(minimum))

    if maximum - minimum == 0:
        return True
    elif maximum - minimum == 1:
        freq = {}.fromkeys([minimum, maximum], 0)
        print(freq)

        for key,val in dict14.items():
            freq[val] += 1

        print(freq)

        if 1 in freq.values():
            return True
        else:
            return False
    else:
        return False


print(isvalidString(str11))

#============================================================================
#Print All subset of arr:
from functools import reduce
lst = [1,2,3,4]
lst1 =[1,5,3,4]
def powerset(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],lst, [[]])

print(powerset(lst))

res2 =[]
for i in range(len(lst)):
        j = i
        while (j < len(lst)):
            sub = lst[i:j+1]
            res2.append(sub)
            j += 1
print('subcommon=',res2)

res3 =[]
for i in range(len(lst1)):
        j = i
        while (j < len(lst1)):
            sub = lst1[i:j+1]
            res3.append(sub)
            j += 1
print('subcommon=',res3)

print(max([i for i in res2 if i in res3],key=len))