def subsets(nums):
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]

    return output

lst=[1,2,3]
out = subsets(lst)
print(out)