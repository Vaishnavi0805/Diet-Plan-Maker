# age = request.form['age']
# Weight = request.form['Weight']
# Height = request.form['Height']
# gender = request.form['gender']
# PA = request.form['PA']
from typing import Final


age=19
Weight=60
Height=175
gender= "male"
h = float(Height)
w = float(Weight)
a = int(age)
LFM = 0
vary_weight="Mild Weight gain"
f_cal=0
PA="Moderate"
Hmeter = (h/100)
# print(Hmeter)
BMI = w/(Hmeter**2)
print(BMI)
if gender == 'female':
    BFP = (1.20*BMI)+(0.23*a)-5.4
    print(BFP)
    # Female LFM
    if BFP >= 14 and BFP <= 18:
        LFM = LFM + 1.0
    elif BFP >= 19 and BFP <= 28:
        LFM = LFM + 0.95
    elif BFP >= 29 and BFP <= 38:
        LFM = LFM + 0.90
    elif BFP >= 38:
        LFM = LFM + 0.85
    BMR = w*0.9*24*LFM
elif gender == 'male':
    BFP = (1.20*BMI)+(0.23*a)-16.2
    print(BFP)
    # Male LFM
    if BFP >= 10 and BFP <= 14:
        LFM = LFM + 1.0
    elif BFP >= 15 and BFP <= 20:
        LFM = LFM + 0.95
    elif BFP >= 21 and BFP <= 28:
        LFM = LFM + 0.90
    elif BFP >= 28:
        LFM = LFM + 0.85
    # print(LFM)
    BMR = w*1.0*24*LFM
# print(BMR)

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


#Weight Choice
if vary_weight =="Mild Weight loss":
    f_cal= Final_calorie-250  
elif vary_weight =="Weight loss":
    f_cal= Final_calorie-500
elif vary_weight =="Mild Weight gain":
    f_cal= Final_calorie+250
elif vary_weight =="Weight gain":
    f_cal= Final_calorie+500
elif vary_weight =="Maintain":
    f_cal= Final_calorie
     
print(f_cal)   



# mild loss= - 0.0357/day
# wt. loss=  -0.0714/day
# mild gain=  +0.0357/day
# wt. gain= +0.0714/day

# 1kg= 7700 cal = 1000 calorie less per day
# halfkg = 3250 = 500 less per day