#We have two sorted lists, and we want to write a function to merge the two lists into one sorted list:
#a = [3, 4, 6, 10, 11, 18]
#b = [1, 5, 7, 12, 13, 19, 21]

a = [3,4,6,10,11,18]
b = [1,5,7,12,13,19,21,30,50]
c = []

while a and b:
    if a[0] < b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))
print (c+b+a)

test_list1 = [3,4,6,10,11,18]
test_list2 = [1,5,7,12,13,19,21,30,50]
res = []
# using naive method
# to combine two sorted lists
size_1 = len(test_list1)
size_2 = len(test_list2)

res = []
i, j = 0, 0

while i < size_1 and j < size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1

    else:
        res.append(test_list2[j])
        j += 1

print(res + test_list1[i:] + test_list2[j:])