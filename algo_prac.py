# # Python3 program to print sums of
# # all possible subsets.

# # Prints sums of all subsets of arr[l..r]


# def subsetSums(arr, l, r, sum=0):

# 	# Print current subset
# 	if l > r:
# 		print(sum, end=" ")
# 		return

# 	# Subset including arr[l]
# 	subsetSums(arr, l + 1, r, sum + arr[l])

# 	# Subset excluding arr[l]
# 	subsetSums(arr, l + 1, r, sum)


# # Driver code
# arr = [5, 4, 3]
# n = len(arr)
# subsetSums(arr, 0, n - 1)

# cal=1000






def subset(array, num):
    result = []
    def find(arr, num, path=()):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)
    find(array, num)
    print(result)
    return result

numbers = [2, 2, 1, 12, 15, 2, 3,45,23,25,24,19,34]
x = 7
for i in range (50,55):
    subset(numbers,i)



# subset(numbers,x)






def percentage(b,l,s,d,whole):

    breakfast=(100 * float(b)/float(whole)*100)
    lunch=(100 * float(l)/float(whole)*100)
    snacks=(100 * float(s)/float(whole)*100)
    dinner=(100 * float(d)/float(whole)*100)
    print(breakfast)
    print(lunch)
    print(snacks)
    print(dinner)

whole=1387
b=25
l=32
s=8
d=35
percentage(b,l,s,d,whole)  