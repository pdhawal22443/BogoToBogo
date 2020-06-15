#===================================================================
cities = {'San Francisco': 'US',
          'London':'UK',
          'Manchester':'UK',
          'Paris':'France',
          'Los Angeles':'US',
          'Seoul':'Korea'}

#o/p = {'US': ['San Francisco', 'Los Angeles'], 'UK': ['London', 'Manchester'], 'France': ['Paris'], 'Korea': ['Seoul']}

res = {}
for key,val in cities.items():
    if val in res:
        res[val].append(key)
    else:
        res[val] = [key]

print(res)

#============================================================
L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296,55,99,300]
#Output = {1: [1, 2, 4, 8], 2: [16, 32, 64, 55, 99], 3: [128, 256, 512, 300], 4: [1024], 5: [32768, 65536], 10: [4294967296]}
res1 = {}
for i in L:
    if len(str(i)) in res1:
        res1[len(str(i))].append(i)
    else:
        res1[len(str(i))] = [i]

print(res1)

#================================================================
#write a code that create a list of (n)**2 for range(10) for even integers:
res = [i**2 for i in range(10) if i%2 == 0]
print(res)

#write a code that create a list of (n)**2 for range(10)
res4 = list(map(lambda x: x**2,range(10)))
print(res4)


#==========================================
#Python Generators

#1st method to create generators using yield
def randomnumber():
    for i in range(200):
        yield i

#create generator object
genobj1 = randomnumber()
print(genobj1.__next__())
print(genobj1.__next__())
print(genobj1.__next__())
print(genobj1.__next__())

#2nd method is to have Generator expression
gen_obj = (i for i in range(100,5000))
print(gen_obj.__next__())
print(gen_obj.__next__())

#=================================================
#list all Prime number upto n

def isprime(num,i=2):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % i == 0:
        return False
    if i*i > num:
        return True
    return isprime(num,i+1)

res11 = list(filter(isprime,range(100)))
print(res11)


#===================================================
'''Hamming distance
In information theory, the Hamming distance between two
 strings of equal length is the number of positions at which the 
 corresponding symbols are different:
    EX - KAROLIN and KATHRIN is 3 => ROL and THR    
 '''

str1 = 'KAROLIN'
str2 = 'KATHRIN'
j = 0
#by for loop
for i in range(len(str1)):
    if str1[i] != str2[i]:
        j = j +1

print(j)

#By List Comprihension
print(len([i for i in range(len(str1)) if str1[i] != str2[i]]))



#============================================================
#print Alternate elements from the list
lst = (1,2,3,4,5,6,7,8,9)
print(lst[::2]) #o/p - (1, 3, 5, 7, 9)

res = []
for i in range(len(lst)):
    if i%2 != 0:
        res.append(lst[i])

print(res) #o/p - [2, 4, 6, 8]

print(type(isprime(4)))



