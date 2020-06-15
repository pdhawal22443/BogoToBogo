toy_price = [1,100,12,5,200,111,10]
money = 50
sum = 0
res = []
def sort(toy_price):
    i = 0
    while i < (len(toy_price) -1):
        if toy_price[i] > toy_price[i+1]:
            toy_price[i+1],toy_price[i] = toy_price[i],toy_price[i+1]
            i = -1
        i += 1
    return toy_price

toy_price = sort(toy_price)
print(toy_price)
for i in toy_price:
    if money > i + sum:
        sum += i
        res.append(i)

print(res)



