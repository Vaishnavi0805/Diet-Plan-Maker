# Age = 19
# Weight = 60
# Height = 175
# gender = "male"
# Hmeter = Height/100
# BMI = Weight/(Hmeter**2)

# print(BMI)
# BFP = (1.20*BMI)+(0.23*Age)-16.2
# print(BFP)

import csv


data = csv.reader(open('dataset.csv','r'))
next(data)
#row = []
list = []
for diet in data:
    # if food in row[3]:
    
    #print(a)
    if diet[0]=='Veg':
        diet[0]=0
    else:
        diet[0]=1
    a=diet[0]
    #print(a)
    #print(diet)
    
    list.append(diet)
#print(list)


#Merge Sort Algorithm
def mergeSort(list):
        if len(list)>1:
            mid=len(list)//2
            left_list=list[:mid]
            right_list=list[mid:]
            mergeSort(left_list)
            mergeSort(right_list)
            i=0
            j=0
            k=0
            while i<len(left_list) and j<len(right_list):
                if left_list[i]<right_list[j]:
                    list[k]=left_list[i]
                    i=i+1
                    k=k+1
                else:
                    list[k]=right_list[j]
                    j=j+1
                    k=k+1
            while i<len(left_list):
                list[k] = left_list[i]
                i=i+1
                k=k+1
            while j<len(right_list):
                list[k] = right_list[j]
                j=j+1
                k=k+1



mergeSort(list)
print(list)
file = open('dataset-copy.csv', 'w+', newline ='')
with file :
    write = csv.writer(file) 
    write.writerows(list) 

