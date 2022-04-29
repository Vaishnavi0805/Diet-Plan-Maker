from flask import Flask, render_template, request, redirect, url_for
import csv
from operator import itemgetter
from itertools import combinations
import csv
import itertools
from typing import final
from operator import itemgetter
import csv
from typing import final

# from prac_csv import percentage

app = Flask(__name__, static_url_path='/static')
app.secret_key = "16516516"


@app.route('/', methods=['GET', 'POST'])  
def cal():
    if request.method == 'POST':
        age = request.form['age']
        Weight = request.form['Weight']
        Height = request.form['Height']
        gender = request.form['gender']
        vary_weight = request.form['vary_weight']
        PA = request.form['PA']
        h = float(Height)
        w = float(Weight)
        a = int(age)
        diet_type=request.form['diet_type']
        # print(item)
        LFM = 0
        
        # Age=19
        # Weight=60
        # Height=175
        # gender= "male"
        # PA="Moderate"
        Hmeter = (h/100)
        # print(Hmeter)
        BMI = w/(Hmeter**2)
        print(BMI)
        if gender == 'male':
            BFP = (1.20*BMI)+(0.23*a)-16.2
            print(BFP)
            # Male LFM
            if BFP >= 10 and BFP <= 14:
                LFM = LFM + 1.0
            elif BFP >= 14 and BFP <= 20:
                LFM = LFM + 0.95
            elif BFP >= 20 and BFP <= 28:
                LFM = LFM + 0.90
            elif BFP >= 28:
                LFM = LFM + 0.85
            # print(LFM)
            BMR = w*1.0*24*LFM
        elif gender == 'female':
            BFP = (1.20*BMI)+(0.23*a)-5.4
            print(BFP)

            # Female LFM
            if BFP >= 14 and BFP <= 18:
                LFM = LFM + 1.0
            elif BFP >= 18 and BFP <= 28:
                LFM = LFM + 0.95
            elif BFP >= 28 and BFP <= 38:
                LFM = LFM + 0.90
            elif BFP >= 38:
                LFM = LFM + 0.85
            BMR = w*0.9*24*LFM
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

        if PA == "Very Light":
            Final_calorie = BMR*1.3
        elif PA == "Light":
            Final_calorie = BMR*1.55
        elif PA == "Moderate":
            Final_calorie = BMR*1.65
        elif PA == "Heavy":
            Final_calorie = BMR*1.80
        elif PA == "Very Heavy":
            Final_calorie = BMR*2.00
        print(Final_calorie)
        # Weight Choice

        if vary_weight == "Mild weight loss(-0.25kg/week)":
            Final_calorie = round(Final_calorie-250)
        elif vary_weight == "Weight loss(-0.5kg/week)":
            Final_calorie = round(Final_calorie-500)
        elif vary_weight == "Mild Weight gain(+0.25kg/week)":
            Final_calorie = round(Final_calorie+250)
        elif vary_weight == "Weight gain(+0.5kg/week)":
            Final_calorie = round(Final_calorie+500)
        elif vary_weight == "Maintain weight(remains same)":
            Final_calorie = round(Final_calorie)

        print(round(Final_calorie))
        # percentage(Final_calorie)
        creating_dicts(diet_type, Final_calorie)
        # percentage(Final_calorie, nv_bcal)

         
        # return render_template("output.html", final=Final_calorie)
        return redirect(url_for('percentage'))
    return render_template('index.html')



abc = []
lunch_list=[]
snacks_list=[]
dinner_list=[]
def creating_dicts(item, Final_calorie):
    Final_calorie = Final_calorie
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
    #item = 'Veg'
    x = []
    for index, elem in enumerate(w):
        if elem == item:
            x.append(index)
        elif item == 'Non-veg':
            for index,item in enumerate(w):
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


    # print(pdict_category)

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
    # print(nv_bindex)

    # lunch index list
    fetch_lindex = list(diet_preference['item_no'][0])
    l = (itemgetter(*lunch_index)(fetch_lindex))
    nv_lindex = [int(i) for i in l]
    # print(nv_lindex)

    # snacks index list
    fetch_sindex = list(diet_preference['item_no'][0])
    s = (itemgetter(*snacks_index)(fetch_sindex))
    nv_sindex = [int(i) for i in s]
    # print(nv_sindex)

    # dinner index list
    fetch_dindex = list(diet_preference['item_no'][0])
    d = (itemgetter(*dinner_index)(fetch_dindex))
    nv_dindex = [int(i) for i in d]
    # print(nv_dindex)

    # breakfast calorie list
    fetch_bcal = list(diet_preference['calories'][0])
    br = (itemgetter(*breakfast_index)(fetch_bcal))
    nv_bcal = [int(i) for i in br]
    # print(nv_bcal)

    # lunch calorie list
    fetch_lcal = list(diet_preference['calories'][0])
    lu = (itemgetter(*lunch_index)(fetch_lcal))
    nv_lcal = [int(i) for i in lu]
    # print(nv_lcal)

    # snacks calorie list
    fetch_scal = list(diet_preference['calories'][0])
    sn = (itemgetter(*snacks_index)(fetch_scal))
    nv_scal = [int(i) for i in sn]
    # print(nv_scal)


    # dinner calorie list
    fetch_dcal = list(diet_preference['calories'][0])
    di = (itemgetter(*dinner_index)(fetch_dcal))
    nv_dcal = [int(i) for i in di]
    # print(nv_dcal)

    # fetch categories
    fetch_bcate = list(diet_preference['category'][0])
    bi = (itemgetter(*breakfast_index)(fetch_bcate))
    nv_bcate = [i for i in bi]
    # print(nv_bcate)

    fetch_lcate = list(diet_preference['category'][0])
    li = (itemgetter(*lunch_index)(fetch_lcate))
    nv_lcate = [i for i in li]
    # print(nv_lcate)

    fetch_scate = list(diet_preference['category'][0])
    si = (itemgetter(*snacks_index)(fetch_scate))
    nv_scate = [i for i in si]
    # print(nv_scate)

    fetch_dcate = list(diet_preference['category'][0])
    di = (itemgetter(*dinner_index)(fetch_dcate))
    nv_dcate = [i for i in di]
    # print(nv_dcate)

    fetch_bnames = list(diet_preference['name'][0])
    bn = (itemgetter(*breakfast_index)(fetch_bnames))
    nv_bname = [i for i in bn]
    # print(nv_bname)

    fetch_lnames = list(diet_preference['name'][0])
    ln = (itemgetter(*lunch_index)(fetch_lnames))
    nv_lname = [i for i in ln]
    # print(nv_lname)

    fetch_snames = list(diet_preference['name'][0])
    sn = (itemgetter(*snacks_index)(fetch_snames))
    nv_sname = [i for i in sn]
    # print(nv_sname)

    fetch_dnames = list(diet_preference['name'][0])
    dn = (itemgetter(*dinner_index)(fetch_dnames))
    nv_dname = [i for i in dn]
    print(f'This is dinner list : {nv_dname}')
    # a= cal()
    # o=len(nv_bcal)
    # subsetSum(xyz, nv_bcal, a)
    percentage(Final_calorie, nv_bcal, nv_bcate, nv_bname, nv_lcal, nv_lcate, nv_lname, nv_scal, nv_scate, nv_sname, nv_dcal,nv_dcate, nv_dname)
    


@app.route('/percentage', methods=['GET', 'POST']) 
def percentage(a,nv_bcal,nv_bcate, nv_bname, nv_lcal, nv_lcate, nv_lname, nv_scal, nv_scate, nv_sname, nv_dcal, nv_dcate, nv_dname):
    Final_calorie = a
    nv_bcate = nv_bcate 
    nv_bname = nv_bname
    nv_lcate = nv_lcate 
    nv_lname = nv_lname
    nv_scate=nv_scate
    nv_sname=nv_sname
    nv_dcate=nv_dcate
    nv_dname=nv_dname
    breakfast=0.25*float(a)
    lunch=0.32*float(a)
    snacks=0.08*float(a)
    dinner=0.35*float(a)
    print(breakfast)
    print(lunch)
    print(snacks)
    print(dinner)
    o = int(breakfast-1)
    print(type(o))
    p = int(breakfast+1)
    llr=int(lunch-25)
    lhr=int(lunch+25)
    slr=int(snacks-10)
    shr=int(snacks+10)
    dlr=int(dinner-30)
    dhr=int(dinner+30)
    xyz = len(nv_bcal)
    print(xyz)
    lunch_length=len(nv_lcal)
    # lunch_length=len(nv_lcal)
    snacks_length=len(nv_scal)
    dinner_length=len(nv_dcal)
    # dinner_length=len(nv_dcal)
    for b in range(o,p):
        var = subsetSum(xyz, nv_bcal, b, nv_bcate, nv_bname)
        abc.append(var)
    final_b_list=(list(itertools.chain.from_iterable(abc)))
    r=len(final_b_list)
    print(r)
    # print("The Breakfast list is ",final_b_list)
    #final_b_list is final breakfast list X001

    for ll in range(llr,lhr):
        lfunc=lunch_subsetSum(lunch_length,nv_lcal,ll,nv_lcate,nv_lname)
        lunch_list.append(lfunc)
    final_l_list=(list(itertools.chain.from_iterable(lunch_list)))
    # print(final_l_list)
    #final_b_list is final lunch list X002

    for ss in range(slr,shr):
        sfunc=snacks_subsetSum(snacks_length,nv_scal,ss,nv_scate,nv_sname)
        snacks_list.append(sfunc)
    final_s_list=(list(itertools.chain.from_iterable(snacks_list)))
    # print(final_s_list)
    #final_s_list is final snack list X003

    for dd in range(dlr,dhr):
        dfunc=dinner_subsetSum(dinner_length,nv_dcal,dd, nv_dcate, nv_dname)
        dinner_list.append(dfunc)
    final_d_list=(list(itertools.chain.from_iterable(dinner_list)))
    # print(final_d_list)
    #final_d_list is final dinner list X004
    random_sets(final_b_list, final_l_list, final_s_list, final_d_list)
    return render_template("sample.html", final = Final_calorie)
    
def subsetSum(xyz, nv_bcal, b,nv_bcate, nv_bname):
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    i = 0
    w=[]
    for i in range(xyz+1):      
        for subset in combinations(nv_bcal, i):
        
            # printing the subset if its sum is x:
            if sum(subset) == b:
                if len(subset) == 3:
                    index_of_element = []
                    t = list(subset)
                    index_of_element.append(nv_bcal.index(t[0]))
                    index_of_element.append(nv_bcal.index(t[1]))
                    index_of_element.append(nv_bcal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element)(nv_bcate))
                    catego = [i for i in li]

                    index_of_element_name = []
                    index_of_element_name.append(nv_bcal.index(t[0]))
                    index_of_element_name.append(nv_bcal.index(t[1]))
                    index_of_element_name.append(nv_bcal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element_name)(nv_bname))
                    nam = [i for i in li]
                    # w=[]
                    if 'Bread' in catego:
                        if 'Fruit' or 'Beverages' in catego:
                            n = "Fruit"
                            m = "Bread"
                            s = "Beverages"
                            if catego.count(n) != 2:
                                if catego.count(m) != 2:
                                    if catego.count(s) != 2:
                                        # print(set(subset))
                                        # print(nam)
                                        w.append(nam)
                                        # w.append(catego)
                                        w.append(list(subset))

                                        
    # final_b_list.append(w)
        if i == 3:
            break
    # final_b_list.append(w)
    m=[]
    # print(w[0])
    for j in w:
        if j not in m:
            m.append(j)
    return m  



#Lunch subsets
# Creating final list for lunch
def lunch_subsetSum(lunch_length,nv_lcal,ll,nv_lcate,nv_lname):
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    i = 0
    w=[]
    for i in range(lunch_length+1):      
        for subset in combinations(nv_lcal, i):
           
            # printing the subset if its sum is x:
            if sum(subset) == ll:
                if len(subset) == 3:
                    index_of_element = []
                    t = list(subset)
                    index_of_element.append(nv_lcal.index(t[0]))
                    index_of_element.append(nv_lcal.index(t[1]))
                    index_of_element.append(nv_lcal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element)(nv_lcate))
                    catego = [i for i in li]

                    index_of_element_name = []
                    index_of_element_name.append(nv_lcal.index(t[0]))
                    index_of_element_name.append(nv_lcal.index(t[1]))
                    index_of_element_name.append(nv_lcal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element_name)(nv_lname))
                    nam = [i for i in li]
                    # w=[]
                    if 'Bread' in catego:
                        if 'Vegetable' or 'Curry' in catego:
                            n = "Vegetable"
                            m = "Curry"
                            s = "Bread"
                            if catego.count(n) != 2:
                                if catego.count(m) != 2:
                                    if catego.count(s) != 2:
                                        # print(set(subset))
                                        # print(nam)
                                        w.append(nam)
                                        # w.append(catego)
                                        w.append(subset)
                                        
    # final_b_list.append(w)
        if i == 3:
            break
    # final_b_list.append(w)
    m=[]
    # print(w[0])
    for j in w:
        if j not in m:
            m.append(j)
    # print(m)  
    return m 

#     # subsetSum(o,nv_bcal,350)
#         # percentage(a)


# Creating final list for snacks 
def snacks_subsetSum(snacks_length,nv_scal,ss,nv_scate,nv_sname):
    i = 0
    w=[]
    for i in range(snacks_length+1):      
        for subset in combinations(nv_scal, i):
           
            # printing the subset if its sum is x:
            if sum(subset) == ss:
                if len(subset) == 2:
                    index_of_element = []
                    t = list(subset)
                    index_of_element.append(nv_scal.index(t[0]))
                    index_of_element.append(nv_scal.index(t[1]))
                    # index_of_element.append(nv_scal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element)(nv_scate))
                    catego = [i for i in li]

                    index_of_element_name = []
                    index_of_element_name.append(nv_scal.index(t[0]))
                    index_of_element_name.append(nv_scal.index(t[1]))
                    # index_of_element_name.append(nv_scal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element_name)(nv_sname))
                    # nam = [i for i in li]
                    w.append(li)
                    # print(nv_sname)
                                        # w.append(catego)
                    w.append(subset)
                                        
    # final_b_list.append(w)
        if i == 3:
            break

    return w
def dinner_subsetSum(dinner_length,nv_dcal,dd,nv_dcate,nv_dname):
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    i = 0
    w=[]
    for i in range(dinner_length+1):      
        for subset in combinations(nv_dcal, i):
           
            # printing the subset if its sum is x:
            if sum(subset) == dd:
                if len(subset) == 3:
                    index_of_element = []
                    t = list(subset)
                    index_of_element.append(nv_dcal.index(t[0]))
                    index_of_element.append(nv_dcal.index(t[1]))
                    index_of_element.append(nv_dcal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element)(nv_dcate))
                    catego = [i for i in li]

                    index_of_element_name = []
                    index_of_element_name.append(nv_dcal.index(t[0]))
                    index_of_element_name.append(nv_dcal.index(t[1]))
                    index_of_element_name.append(nv_dcal.index(t[2]))
                    # print("This is subset index", index_of_element)
                    li = (itemgetter(*index_of_element_name)(nv_dname))
                    nam = [i for i in li]
                    # w=[]
                    
                    w.append(nam)
                                        # w.append(catego)
                    w.append(subset)
                                        
    # final_b_list.append(w)
        if i == 3:
            break
    # final_b_list.append(w)
    m=[]
    # print(w[0])
    for j in w:
        if j not in m:
            m.append(j)
    # print(m)  
    return m 

import random
def random_sets(final_b_list, final_l_list, final_s_list, final_d_list):
    b=[]
    l=[]
    sn=[]
    d=[]
    choice_b_list = []
    choice_l_list = []
    choice_s_list = []
    choice_d_list = []
    #BREAKFAST
    for bbb in final_b_list:
    # # #     # j = final_b_list.index(i)
    # # #     # kgf.append(j)
        if final_b_list.index(bbb) %2 == 0:
            b.append(bbb)
        k = random.choices(b) #k=[appam,.....]
        s = final_b_list.index(k[0]) #s=index of random from final...
        u = final_b_list[s+1]
    choice_b_list.append(k[0])
    choice_b_list.append(u)
    print("Breakfast: ",choice_b_list)
    #LUNCH
    for lll in final_l_list:
    # # #     # j = final_b_list.index(i)
    # # #     # kgf.append(j)
        if final_l_list.index(lll) %2 == 0:
            l.append(lll)
        k = random.choices(l) #k=[appam,.....]
        s = final_l_list.index(k[0]) #s=index of random from final...
        u = final_l_list[s+1]
    choice_l_list.append(k[0])
    choice_l_list.append(u)
    print("Lunch: ",choice_l_list)
    #SNACKS
    for sss in final_s_list:
    # # #     # j = final_b_list.index(i)
    # # #     # kgf.append(j)
        # s=[]
        if final_s_list.index(sss) %2 == 0:
            sn.append(sss)
        k = random.choices(sn) #k=[appam,.....]
        s = final_s_list.index(k[0]) #s=index of random from final...
        u = final_s_list[s+1]
    choice_s_list.append(k[0])
    choice_s_list.append(u)
    print("Snacks: ",choice_s_list)
    # #DINNER
    for ddd in final_d_list:
    # # #     # j = final_b_list.index(i)
    # # #     # kgf.append(j)
        if final_d_list.index(ddd) %2 == 0:
            d.append(ddd)
        k = random.choices(d) #k=[appam,.....]
        s = final_d_list.index(k[0]) #s=index of random from final...
        u = final_d_list[s+1]
    choice_d_list.append(k[0])
    choice_d_list.append(u)
    print("Dinner: ",choice_d_list)
    
    
    
#
# randomly generated subset of food item and its corresponding calorie subset.
    # j = random.choices(kgf)
    # print(j)


        # final_b_list usme ka index and random
if __name__ == "__main__":
    app.run(debug=True)