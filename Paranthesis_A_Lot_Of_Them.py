'''Parenthesis, a lot of them
Write a function that outputs a list of tuples [(an opening parenthesis, the corresponding closing parenthesis), () ...].
 The tuple should be an index of the position of parenthesis.
  For example, "(())()", the list should be [(0,3),(1,2),(4,5)]'''

str = '(())()'
res = []
stack = []
for i in range(len(str)):
    if str[i] is '(':
        stack.append(i)
    else:
        res.append((stack.pop(),i))

print(res)

