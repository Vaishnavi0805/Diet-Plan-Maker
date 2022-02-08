from flask import Flask, request

def cal():
    # Age=request.form['Age']
    # Weight=request.form['Weight']
    # Height=request.form['Height']
    # gender=request.form['gender']
    Age=19
    Weight=60
    Height=175
    gender= "male"
    Hmeter=Height/100
    BMI = Weight/(Hmeter**2)
    print(BMI)
    if gender=='female':
        BFP=(1.20*BMI)+(0.23*Age)-5.4
        print(BFP)
        #Female LFM
        if BFP >= 14 and BFP <= 18:
            LFM = 1.0
        elif BFP >= 19 and BFP <= 28:
            LFM = 0.95 
        elif BFP >= 29 and BFP <= 38:
            LFM = 0.90 
        elif BFP >= 38:
            LFM = 0.85
        BMR= Weight*0.9*24*LFM
    elif gender=='male':
        BFP=(1.20*BMI)+(0.23*Age)-16.2
        print(BFP)
        #Male LFM
        if BFP >= 10 and BFP <= 14:
            LFM = 1.0 
        elif BFP >= 15 and BFP <= 20:
            LFM = 0.95 
        elif BFP >= 21 and BFP <= 28:
            LFM = 0.90 
        elif BFP >= 28:
            LFM = 0.85 
        print(LFM)
        BMR = Weight*1.0*24*LFM
    print(BMR)

cal()
