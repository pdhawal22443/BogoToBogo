lst = [{'key1':10,'key2':20},{'key1':30,'key2':1},{'key1':88,'key2':4}]
#print the dictionary with max value of key2
temp = {}
for i in lst:
    if 'key2' in temp :
        if i['key2'] > temp['key2']:
            temp = i
    else:
        temp = i

print(temp)


