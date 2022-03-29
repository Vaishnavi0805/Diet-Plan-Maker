import csv
# open the file in read mode
filename = open('dataset.csv', 'r')
# creating dictreader object
file = csv.DictReader(filename)
my_dict={'diet_type':'0','item_no':'0','name':'0', 'category': '0', 'meal': '0', 'ingredients' : '0', 'serving_size': '0', 'calories':'0','cholesterol':'0', 'total_fats':'0', 'protein':'0', 'carbohydrates':'0','sugar':'0','calcium':'0', 'sodium': '0', 'potassium': '0', 'glucose': '0'}
# creating empty lists
diet_type = []
item_no = []
name = []
category=[]
meal=[]
ingredients=[]
serving_size=[]
calories=[]
cholesterol=[]
total_fats=[]
protein=[]
carbohydrates=[]
sugar=[]
calcium=[]
sodium=[]
potassium=[]
glucose=[]

 
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
my_dict['total_fats']= total_fats
my_dict['protein']=protein
my_dict['carbohydrates']= carbohydrates
my_dict['sugar']=sugar
my_dict['calcium']=calcium
my_dict['sodium']=sodium
my_dict['potassium']=potassium
my_dict['glucose']=glucose
 
# printing lists
#my_dict={'diet_type':[]}
print(my_dict)
