# age = request.form['age']
# Weight = request.form['Weight']
# Height = request.form['Height']
# gender = request.form['gender']
# PA = request.form['PA']
# from typing import Final


# age=19
# Weight=60
# Height=175
# gender= "male"
# h = float(Height)
# w = float(Weight)
# a = int(age)
# LFM = 0
# vary_weight="Mild Weight gain"
# f_cal=0
# PA="Moderate"
# Hmeter = (h/100)
# # print(Hmeter)
# BMI = w/(Hmeter**2)
# print(BMI)
# if gender == 'female':
#     BFP = (1.20*BMI)+(0.23*a)-5.4
#     print(BFP)
#     # Female LFM
#     if BFP >= 14 and BFP <= 18:
#         LFM = LFM + 1.0
#     elif BFP >= 19 and BFP <= 28:
#         LFM = LFM + 0.95
#     elif BFP >= 29 and BFP <= 38:
#         LFM = LFM + 0.90
#     elif BFP >= 38:
#         LFM = LFM + 0.85
#     BMR = w*0.9*24*LFM
# elif gender == 'male':
#     BFP = (1.20*BMI)+(0.23*a)-16.2
#     print(BFP)
#     # Male LFM
#     if BFP >= 10 and BFP <= 14:
#         LFM = LFM + 1.0
#     elif BFP >= 15 and BFP <= 20:
#         LFM = LFM + 0.95
#     elif BFP >= 21 and BFP <= 28:
#         LFM = LFM + 0.90
#     elif BFP >= 28:
#         LFM = LFM + 0.85
#     # print(LFM)
#     BMR = w*1.0*24*LFM
# # print(BMR)

# if PA == "Very Light":
#     Final_calorie = BMR*1.3
# elif PA == "Light":
#     Final_calorie = BMR*1.55
# elif PA == "Moderate":
#     Final_calorie = BMR*1.65
# elif PA == "Heavy":
#     Final_calorie = BMR*1.80
# elif PA == "Very Heavy":
#     Final_calorie = BMR*2.00
# print(Final_calorie)


# #Weight Choice
# if vary_weight =="Mild Weight loss":
#     f_cal= Final_calorie-250
# elif vary_weight =="Weight loss":
#     f_cal= Final_calorie-500
# elif vary_weight =="Mild Weight gain":
#     f_cal= Final_calorie+250
# elif vary_weight =="Weight gain":
#     f_cal= Final_calorie+500
# elif vary_weight =="Maintain":
#     f_cal= Final_calorie

# print(f_cal)


# # mild loss= - 0.0357/day
# # wt. loss=  -0.0714/day
# # mild gain=  +0.0357/day
# # wt. gain= +0.0714/day

# # 1kg= 7700 cal = 1000 calorie less per day
# # halfkg = 3250 = 500 less per day

# # org_list=[45,78,65,85,96,1,54,3,6]

# # filtered_list=list(filter(lambda x: (x%2!=0), org_list))

# def SubsetSum(set, n, sum) :
#    # Base Cases
#    if (sum == 0) :
#       return True
#    if (n == 0 and sum != 0) :
#       return False
#    # ignore if last element is > sum
#    if (set[n - 1] > sum) :
#       return SubsetSum(set, n - 1, sum)
#    # else,we check the sum
#    # (1) including the last element
#    # (2) excluding the last element
#    return SubsetSum(set, n-1, sum) or SubsetSum(set, n-1, subset[n-1])
# # main
# set = [2, 14, 6, 22, 4, 8]
# sum = 10
# n = len(set)
# if (SubsetSum(set, n, sum) == True) :
#    print("Found a subset with given sum")
# else :
#    print("No subset with given sum")

# SubsetSum(set, n, sum)

# A recursive solution for subset sum
# problem

# Returns true if there is a subset
# of set[] with sun equal to given sum
# def isSubsetSum(set, n, sum) :

# 	# Base Cases
# 	if (sum == 0) :
# 		return True
# 	if (n == 0 and sum != 0) :
# 		return False

# 	# If last element is greater than
# 	# sum, then ignore it
# 	if (set[n - 1] > sum) :
# 		return isSubsetSum(set, n - 1, sum)

# 	# else, check if sum can be obtained
# 	# by any of the following
# 	# (a) including the last element
# 	# (b) excluding the last element
# 	return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])


# # Driver program to test above function
# set = [3, 34, 4, 12, 5, 2]
# sum = 9
# n = len(set)
# if (isSubsetSum(set, n, sum) == True) :
# 	print("Found a subset with given sum")
#     print(subset)
# else :
# 	print("No subset with given sum")

# This code is contributed by Nikita Tiwari.

# def subset_sum(arr, res, sum):
#     if sum == 0:
#         return True
#     if sum < 0:
#         return False
#     if len(arr) == 0 and sum!= 0 :
#         return False
#         arr.pop(0);
#     if len(arr) > 0:
#         res.append(arr[0])
#         select = subset_sum(arr, sum-arr[0], res)
#         reject = subset_sum(arr, res, sum)
#         return reject or sum
# arr=[1,2,3,4,5]
# sum=9
# res=[]
# subset_sum(arr,res,sum)

# def twentyone(array, num=21):
#     if num < 0:
#         return
#     if len(array) == 0:
#         if num == 0:
#             yield []
#         return
#     for solution in twentyone(array[1:], num):
#         yield solution
#     for solution in twentyone(array[1:], num - array[0]):
#         yield [array[0]] + solution

# # array=[1,2,3,6,4,15]
# # num=21
# twentyone([1,2,3,6,4,15])
#
# Python code with time complexity
# O(2^n)to print all subsets whose
# sum is equal to a given value
from itertools import combinations

def subsetSum(n, arr, a):

	# Iterating through all possible
	# subsets of arr from lengths 0 to n:
        for i in range(n+1):
            for subset in combinations(arr, i):

                # printing the subset if its sum is x:
                
                if sum(subset) == a:
                    print(subset)
                # else:
                #     print("No possible combinations")
        

            
        

# Driver Code:
n = 6
arr = [10, 21, 25, 50, 1000, 90]
x = 80
o=x-5
p=x+5
for a in range(o,p):  
    subsetSum(n, arr, a)
 
