#Find kth largest element using quick sort
import pdb

#1st quicksort should be implimented , partition part will remain same but interface will have soem changes

def findKthElement(nums,k):
    return quick_select(nums,0,len(nums)-1,k)

def quick_select(nums,start,n,k):
    pos = partition(nums,start,n)
    if pos == k-1:
        return nums[pos]
    elif pos >= k:
        return quick_select(nums,start,pos-1,k)
    return quick_select(nums,pos+1,n,k)

def partition(nums,left,right):
    pivot = nums[right] #taking the rightmost element as initial pivot
    i = left
    for j in range(left,right):
        if nums[j] > pivot:
            nums[j],nums[i] = nums[i],nums[j]
            i += 1
    nums[right],nums[i] = nums[i],nums[right]
    return i

lst = [3,2,1,5,6,4]
#[1,2,3,4,5,6]
res = findKthElement(lst,4)
print(res)



