# # age = request.form['age']
# # Weight = request.form['Weight']
# # Height = request.form['Height']
# # gender = request.form['gender']
# # PA = request.form['PA']
# # from typing import Final


# # age=19
# # Weight=60
# # Height=175
# # gender= "male"
# # h = float(Height)
# # w = float(Weight)
# # a = int(age)
# # LFM = 0
# # vary_weight="Mild Weight gain"
# # f_cal=0
# # PA="Moderate"
# # Hmeter = (h/100)
# # # print(Hmeter)
# # BMI = w/(Hmeter**2)
# # print(BMI)
# # if gender == 'female':
# #     BFP = (1.20*BMI)+(0.23*a)-5.4
# #     print(BFP)
# #     # Female LFM
# #     if BFP >= 14 and BFP <= 18:
# #         LFM = LFM + 1.0
# #     elif BFP >= 19 and BFP <= 28:
# #         LFM = LFM + 0.95
# #     elif BFP >= 29 and BFP <= 38:
# #         LFM = LFM + 0.90
# #     elif BFP >= 38:
# #         LFM = LFM + 0.85
# #     BMR = w*0.9*24*LFM
# # elif gender == 'male':
# #     BFP = (1.20*BMI)+(0.23*a)-16.2
# #     print(BFP)
# #     # Male LFM
# #     if BFP >= 10 and BFP <= 14:
# #         LFM = LFM + 1.0
# #     elif BFP >= 15 and BFP <= 20:
# #         LFM = LFM + 0.95
# #     elif BFP >= 21 and BFP <= 28:
# #         LFM = LFM + 0.90
# #     elif BFP >= 28:
# #         LFM = LFM + 0.85
# #     # print(LFM)
# #     BMR = w*1.0*24*LFM
# # # print(BMR)

# # if PA == "Very Light":
# #     Final_calorie = BMR*1.3
# # elif PA == "Light":
# #     Final_calorie = BMR*1.55
# # elif PA == "Moderate":
# #     Final_calorie = BMR*1.65
# # elif PA == "Heavy":
# #     Final_calorie = BMR*1.80
# # elif PA == "Very Heavy":
# #     Final_calorie = BMR*2.00
# # print(Final_calorie)


# # #Weight Choice
# # if vary_weight =="Mild Weight loss":
# #     f_cal= Final_calorie-250
# # elif vary_weight =="Weight loss":
# #     f_cal= Final_calorie-500
# # elif vary_weight =="Mild Weight gain":
# #     f_cal= Final_calorie+250
# # elif vary_weight =="Weight gain":
# #     f_cal= Final_calorie+500
# # elif vary_weight =="Maintain":
# #     f_cal= Final_calorie

# # print(f_cal)


# # # mild loss= - 0.0357/day
# # # wt. loss=  -0.0714/day
# # # mild gain=  +0.0357/day
# # # wt. gain= +0.0714/day

# # # 1kg= 7700 cal = 1000 calorie less per day
# # # halfkg = 3250 = 500 less per day

# # # org_list=[45,78,65,85,96,1,54,3,6]

# # # filtered_list=list(filter(lambda x: (x%2!=0), org_list))

# # def SubsetSum(set, n, sum) :
# #    # Base Cases
# #    if (sum == 0) :
# #       return True
# #    if (n == 0 and sum != 0) :
# #       return False
# #    # ignore if last element is > sum
# #    if (set[n - 1] > sum) :
# #       return SubsetSum(set, n - 1, sum)
# #    # else,we check the sum
# #    # (1) including the last element
# #    # (2) excluding the last element
# #    return SubsetSum(set, n-1, sum) or SubsetSum(set, n-1, subset[n-1])
# # # main
# # set = [2, 14, 6, 22, 4, 8]
# # sum = 10
# # n = len(set)
# # if (SubsetSum(set, n, sum) == True) :
# #    print("Found a subset with given sum")
# # else :
# #    print("No subset with given sum")

# # SubsetSum(set, n, sum)

# # A recursive solution for subset sum
# # problem

# # Returns true if there is a subset
# # of set[] with sun equal to given sum
# # def isSubsetSum(set, n, sum) :

# # 	# Base Cases
# # 	if (sum == 0) :
# # 		return True
# # 	if (n == 0 and sum != 0) :
# # 		return False

# # 	# If last element is greater than
# # 	# sum, then ignore it
# # 	if (set[n - 1] > sum) :
# # 		return isSubsetSum(set, n - 1, sum)

# # 	# else, check if sum can be obtained
# # 	# by any of the following
# # 	# (a) including the last element
# # 	# (b) excluding the last element
# # 	return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])


# # # Driver program to test above function
# # set = [3, 34, 4, 12, 5, 2]
# # sum = 9
# # n = len(set)
# # if (isSubsetSum(set, n, sum) == True) :
# # 	print("Found a subset with given sum")
# #     print(subset)
# # else :
# # 	print("No subset with given sum")

# # This code is contributed by Nikita Tiwari.

# # def subset_sum(arr, res, sum):
# #     if sum == 0:
# #         return True
# #     if sum < 0:
# #         return False
# #     if len(arr) == 0 and sum!= 0 :
# #         return False
# #         arr.pop(0);
# #     if len(arr) > 0:
# #         res.append(arr[0])
# #         select = subset_sum(arr, sum-arr[0], res)
# #         reject = subset_sum(arr, res, sum)
# #         return reject or sum
# # arr=[1,2,3,4,5]
# # sum=9
# # res=[]
# # subset_sum(arr,res,sum)

# # def twentyone(array, num=21):
# #     if num < 0:
# #         return
# #     if len(array) == 0:
# #         if num == 0:
# #             yield []
# #         return
# #     for solution in twentyone(array[1:], num):
# #         yield solution
# #     for solution in twentyone(array[1:], num - array[0]):
# #         yield [array[0]] + solution

# # # array=[1,2,3,6,4,15]
# # # num=21
# # twentyone([1,2,3,6,4,15])
# #
# # Python code with time complexity
# # O(2^n)to print all subsets whose
# # sum is equal to a given value
# from itertools import combinations

# def subsetSum(n, arr, a):

# 	# Iterating through all possible
# 	# subsets of arr from lengths 0 to n:
#         for i in range(n+1):
#             for subset in combinations(arr, i):

#                 # printing the subset if its sum is x:
                
#                 if sum(subset) == a:
#                     print(subset)
#                 # else:
#                 #     print("No possible combinations")
        


                    

# # Driver Code:
# n = 6
# arr = [10, 21, 25, 50, 1000, 90]
# x = 80
# o=x-5
# p=x+5
# for a in range(o,p):  
#     subsetSum(n, arr, a)
 
from operator import itemgetter
from itertools import combinations
import csv
# open the file in read mode
filename = open('dataset.csv', 'r')
# creating dictreader object
file = csv.DictReader(filename)
my_dict = {'diet_type': '0', 'item_no': '0', 'name': '0', 'category': '0', 'meal': '0', 'ingredients': '0', 'serving_size': '0', 'calories': '0',
           'cholesterol': '0', 'total_fats': '0', 'protein': '0', 'carbohydrates': '0', 'sugar': '0', 'calcium': '0', 'sodium': '0', 'potassium': '0', 'glucose': '0'}
# creating empty lists
diet_type = []
item_no = []
name = []
category = []
meal = []
ingredients = []
serving_size = []
calories = []
cholesterol = []
total_fats = []
protein = []
carbohydrates = []
sugar = []
calcium = []
sodium = []
potassium = []
glucose = []


# iterating over each row and append
# values to empty list
for col in file:
    diet_type.append(col['diet_type'])
    item_no.append(col['item_no'])
    name.append(col['name'])
    category.append(col['category'])
    meal.append(col['meal'])
    ingredients.append(col['ingredients'])
    serving_size.append(col['serving_size'])
    calories.append(col['calories'])
    cholesterol.append(col['cholesterol (mg)'])
    total_fats.append(col['total_fats (g)'])
    protein.append(col['protein (g)'])
    carbohydrates.append(col['carbohydrates (g)'])
    sugar.append(col['sugar (g)'])
    calcium.append(col['calcium'])
    sodium.append(col['sodium (mg)'])
    potassium.append(col['potassium (mg)'])
    glucose.append(col['glucose'])

my_dict['diet_type'] = diet_type
my_dict['item_no'] = item_no
my_dict['name'] = name
my_dict['category'] = category
my_dict['meal'] = meal
my_dict['ingredients'] = ingredients
my_dict['serving_size'] = serving_size
my_dict['calories'] = calories
my_dict['cholesterol'] = cholesterol
my_dict['total_fats'] = total_fats
my_dict['protein'] = protein
my_dict['carbohydrates'] = carbohydrates
my_dict['sugar'] = sugar
my_dict['calcium'] = calcium
my_dict['sodium'] = sodium
my_dict['potassium'] = potassium
my_dict['glucose'] = glucose


# Accessing index numbers of prefered items.
w = my_dict['diet_type']
item = 'Veg'
x = []
for index, elem in enumerate(w):
    if elem == item:
        x.append(index)


# print(x)

# Obtaing elements from original dictionary
itemno = my_dict['item_no']
names = my_dict['name']
category = my_dict['category']
meal = my_dict['meal']
ingredients = my_dict['ingredients']
servingsize = my_dict['serving_size']
calories = my_dict['calories']
cholesterol = my_dict['cholesterol']
total_fats = my_dict['total_fats']
protein = my_dict['protein']
carbohydrates = my_dict['carbohydrates']
sugar = my_dict['sugar']
calcium = my_dict['calcium']
sodium = my_dict['sodium']
potassium = my_dict['potassium']
glucose = my_dict['glucose']

# print(overall_names)

# Extracting elements having same index numbers as prefered items.
pdict_item_no = itemgetter(*x)(itemno)
pdict_names = itemgetter(*x)(names)
pdict_category = itemgetter(*x)(category)
pdict_meal = itemgetter(*x)(meal)
pdict_ingredients = itemgetter(*x)(ingredients)
pdict_servingsize = itemgetter(*x)(servingsize)
pdict_calories = itemgetter(*x)(calories)
pdict_cholesterol = itemgetter(*x)(cholesterol)
pdict_total_fats = itemgetter(*x)(total_fats)
pdict_protein = itemgetter(*x)(protein)
pdict_carbohydrates = itemgetter(*x)(carbohydrates)
pdict_sugar = itemgetter(*x)(sugar)
pdict_calcium = itemgetter(*x)(calcium)
pdict_sodium = itemgetter(*x)(sodium)
pdict_potassium = itemgetter(*x)(potassium)
pdict_glucose = itemgetter(*x)(glucose)


# print(pdict_names)

# Creating veg/non-veg dictionary
diet_preference = {}
diet_preference['item_no'] = [pdict_item_no]
diet_preference['name'] = [pdict_names]
diet_preference['category'] = [pdict_category]
diet_preference['meal'] = [pdict_meal]
diet_preference['ingredients'] = [pdict_ingredients]
diet_preference['serving_size'] = [pdict_servingsize]
diet_preference['calories'] = [pdict_calories]
diet_preference['cholesterol'] = [pdict_cholesterol]
diet_preference['total_fats'] = [pdict_total_fats]
diet_preference['protein'] = [pdict_protein]
diet_preference['carbohydrates'] = [pdict_carbohydrates]
diet_preference['sugar'] = [pdict_sugar]
diet_preference['calcium'] = [pdict_calcium]
diet_preference['sodium'] = [pdict_sodium]
diet_preference['potassium'] = [pdict_potassium]
diet_preference['glucose'] = [pdict_glucose]

# print(diet_preference)
# print(diet_preference['name'][0][8])


# For meals dictionary


# Breakfast
breakfast = diet_preference['meal']
b_meal = 'Breakfast'
breakfast_index = []
for index, elem in enumerate(breakfast[0][:]):
    if elem == b_meal:
        breakfast_index.append(index)

breakfast_names = itemgetter(*breakfast_index)(pdict_names)
# print(breakfast_names)
# print(breakfast_index)

# Lunch
lunch = diet_preference['meal']
l_meal = 'Lunch'
lunch_index = []
for index, elem in enumerate(lunch[0][:]):
    if elem == l_meal:
        lunch_index.append(index)

lunch_names = itemgetter(*lunch_index)(pdict_names)

# print(lunch_names)

# Snacks
snacks = diet_preference['meal']
s_meal = 'Snacks'
snacks_index = []
for index, elem in enumerate(snacks[0][:]):
    if elem == s_meal:
        snacks_index.append(index)

snacks_names = itemgetter(*snacks_index)(pdict_names)
# print(snacks_names)

# Dinner
dinner = diet_preference['meal']
d_meal = 'Dinner'
dinner_index = []
for index, elem in enumerate(dinner[0][:]):
    if elem == d_meal:
        dinner_index.append(index)
# print(dinner_index)

dinner_names = itemgetter(*dinner_index)(pdict_names)
# print(dinner_names)

meal_dict = {}
meal_dict['Breakfast'] = [breakfast_names]
meal_dict['Lunch'] = [lunch_names]
meal_dict['Snacks'] = [snacks_names]
meal_dict['Dinner'] = [dinner_names]

# print(meal_dict)

# breakfast index list
fetch_bindex = list(diet_preference['item_no'][0])
b = (itemgetter(*breakfast_index)(fetch_bindex))
nv_bindex = [int(i) for i in b]
print(nv_bindex)

# lunch index list
fetch_lindex = list(diet_preference['item_no'][0])
l = (itemgetter(*lunch_index)(fetch_lindex))
nv_lindex = [int(i) for i in l]
print(nv_lindex)

# snacks index list
fetch_sindex = list(diet_preference['item_no'][0])
s = (itemgetter(*snacks_index)(fetch_sindex))
nv_sindex = [int(i) for i in s]
print(nv_sindex)

# dinner index list
fetch_dindex = list(diet_preference['item_no'][0])
d = (itemgetter(*dinner_index)(fetch_dindex))
nv_dindex = [int(i) for i in d]
print(nv_dindex)

# breakfast calorie list
fetch_bcal = list(diet_preference['calories'][0])
br = (itemgetter(*breakfast_index)(fetch_bcal))
nv_bcal = [int(i) for i in br]
print(nv_bcal)

# lunch calorie list
fetch_lcal = list(diet_preference['calories'][0])
lu = (itemgetter(*lunch_index)(fetch_lcal))
nv_lcal = [int(i) for i in lu]
print(nv_lcal)

# snacks calorie list
fetch_scal = list(diet_preference['calories'][0])
sn = (itemgetter(*snacks_index)(fetch_scal))
nv_scal = [int(i) for i in sn]
print(nv_scal)


# dinner calorie list
fetch_dcal = list(diet_preference['calories'][0])
di = (itemgetter(*dinner_index)(fetch_dcal))
nv_dcal = [int(i) for i in di]
print(nv_dcal)

bcal=[[120,320,400],[100,55,65,85,95],[45,23,56,20]]
# print(bcal[0])
def subsetSum(xyz, bcal, a):
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    for i in range(xyz+1):
        for subset in combinations(bcal, i):
            # printing the subset if its sum is x:
            if sum(subset) == a:
                print("This is subset", subset)
                break

            # if len(subset) == 10:
            #     break
            # limit=10
            # # else:
            # #     print("No possible combinations")
            # for item in enumerate(i):
            #     print(item)
            #     if item == limit:
            #         break

# Driver Code:
# n = 6
# arr = [10, 21, 25, 50, 1000, 90]
# x = 80


def percentage(b,whole):

    breakfast1 = (100*float(b)/float(whole)*100)
    # lunch1 = (100 * float(l)/float(whole)*100)
    # snacks1 = (100 * float(s)/float(whole)*100)
    # dinner1 = (100 * float(d)/float(whole)*100)
    # print(breakfast1)
    # print(lunch1)
    # print(snacks1)
    # print(dinner1)
    o = int(breakfast1-5)
    p = int(breakfast1+5)
    xyz = len(nv_bcal)
    for a in range(o, p):
        subsetSum(xyz, bcal, a)


whole = 1000
b = 25
# l = 32
# s = 8
# d = 35
percentage(b, whole)

print()
