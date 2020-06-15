map1 = {}

def updateFrequency(test1):
    if test1 in map1:
        map1[test1] += 1
    else:
        map1[test1] = 1


ss = """I figured it out I figured it out from black and white Seconds and hours Maybe they had to take some time"""

word = ss.split(" ")
for i in word:
    updateFrequency(i)

print(map1)


