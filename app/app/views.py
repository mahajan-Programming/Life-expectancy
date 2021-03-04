from django.shortcuts import render
import pandas as pd
import joblib 

def home(request):
    if request.method == "POST":
        AM = request.POST['AM']
        ID = request.POST['ID']
        PM = request.POST['PM']
        Alcohol = request.POST['Alcohol']
        HB = request.POST['HB']
        M = request.POST['M']
        BMI = request.POST['BMI']
        Deaths = request.POST['Deaths']
        Polio = request.POST['Polio']
        TE = request.POST['TE']
        DIP = request.POST['DIP']
        AIDS = request.POST['AIDS']
        POPU = request.POST['POPU']
        a19 = request.POST['19']
        a9 = request.POST['9']
        INCOME = request.POST['INCOME']
        SCHOOLING = request.POST['SCHOOLING']
        GDP = request.POST['GDP']
        arr = [AM,ID,Alcohol,PM,HB,M,BMI,Deaths,Polio,TE,DIP,AIDS,GDP,POPU,a19,a9,INCOME,SCHOOLING]
        data = pd.DataFrame(data=arr
    #     columns=['Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure',
    #    'Hepatitis B', 'Measles ', ' BMI ', 'under-five deaths ', 'Polio',
    #    'Total expenditure', 'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
    #    ' thinness  1-19 years', ' thinness 5-9 years',
    #    'Income composition of resources', 'Schooling']
       )
        print("heloo")
        with open('predict_life.pkl', 'rb') as f:
            knn_from_joblib = joblib.load(f)
        # knn_from_joblib = joblib.load('predict_life.pkl')  
        result = knn_from_joblib.predict(data).mean()
        print("printed")
        result =int(result)
        return render(request,"results.html",{"result":result})
    print("home")
    return render(request,"home.html",{})

def results(request):
    return render(request,"results.html",{})