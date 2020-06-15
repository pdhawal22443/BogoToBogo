#there are 3 types of brackets in python
#[] , () , {}
temp = []
def validateParantheses(test):
    for i in test:
        if i is '{' or i is '[' or i is '(':
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            p1 = temp.pop()
            if bracketmatch(p1,i) is False:
                return False
    return len(temp) == 0


def bracketmatch(test1,test2):
    if test1 is '{' and test2 is '}' or test1 is '[' and test2 is ']' or test1 is '(' and test2 is ')':
        return True
    else:
        return False

print(validateParantheses('{([[[{{}}]]])([{}])}'))

list = ['Black', 'holes', 'are', 'where', 'God', 'divided', 'by', 'zero']
str = " ".join(list)

print(str)
