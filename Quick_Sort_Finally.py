import pdb
lst = [1,9,2,20,15,7,6,0,4]

def quick_sort(lst,low,hi):
    #to check if we have more than 1 element
    if low < hi:
        #this partion function will give us a pivot in list where
        #all no. greater than pivot will be in right and all no. smaller than pivot will be in right
        p = partition(lst,low,hi)
        #quick_sort(lst,low,p-1)
        #quick_sort(lst,p+1,hi)

def partition(lst1,low,hi):
    #we are setting at the middle of the list
    pivot_index = (low+hi) // 2
    pivot_value = lst1[pivot_index]

    #in start put the pivot value to the left most of the list
    lst1[low],lst1[pivot_index] = lst1[pivot_index],lst1[low]

    border = low

    for i in range(low,hi+1):
        if lst1[i] < pivot_value:
            border += 1
            lst1[border] ,lst1[i] = lst1[i],lst1[border]
    lst1[low],lst1[border] = lst1[border],lst1[low]

    return border
#pdb.set_trace()
quick_sort(lst,0,len(lst)-1)
print(lst)


