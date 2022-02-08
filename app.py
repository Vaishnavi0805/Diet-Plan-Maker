from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='/static')
app.secret_key = "16516516"


@app.route('/', methods = ['GET', 'POST'])
def cal():
    if request.method == 'POST':
        age = request.form['age']
        Weight = request.form['Weight']
        Height = request.form['Height']
        gender = request.form['gender']
        PA = request.form['PA']
        # Age=19
        # Weight=60
        # Height=175
        # gender= "male"
        # PA="Moderate"
        Hmeter=int(Height/100)
        #print(Hmeter)
        BMI = Weight/(Hmeter**2)
        print(BMI)
        if gender=='female':
            BFP=(1.20*BMI)+(0.23*age)-5.4
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
            BFP=(1.20*BMI)+(0.23*age)-16.2
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

        if PA=="Very Light":
            Final_calorie=BMR*1.3
        elif PA=="Light":
            Final_calorie=BMR*1.55
        elif PA=="Moderate":
            Final_calorie=BMR*1.65
        elif PA=="Heavy":
            Final_calorie=BMR*1.80 
        elif PA=="Very Heavy":
            Final_calorie=BMR*2.00  
        print(Final_calorie)
        return render_template("output.html", final = Final_calorie)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)