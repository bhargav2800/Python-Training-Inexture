from ast import Return
from curses.ascii import HT
import re
from django.shortcuts import render,HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import joblib
import os
import  numpy as np
import pickle
from keras.models import load_model


# Create your views here.
def index(request):
    return render(request, "index.html")

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, "stroke_form.html")
        else:
            return HttpResponse("Kindly register Your self First ! ")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['Password']
        cpassword = request.POST['CPassword']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()

        messages.success(request, "Your Account has been created Successfully ! ")

        return render(request,"index.html")

    elif request.method == 'GET':
        return render(request,'register.html')
    else:
        return HttpResponse("An Exception Occured! Registraion has Not Been Done")

def stroke_predict(request):
    gender=int(request.POST.get('gender'))
    age=int(request.POST.get('age'))
    hypertension=int(request.POST.get('hypertension'))
    heart_disease = int(request.POST.get('heart_disease'))
    ever_married = int(request.POST.get('ever_married'))
    work_type = int(request.POST.get('work_type'))
    # Residence_type = int(request.POST.get('Residence_type'))
    avg_glucose_level = float(request.POST.get('avg_glucose_level'))
    # bmi = float(request.POST.get('bmi'))
    smoking_status = int(request.POST.get('smoking_status'))

    x=np.array([gender,age,hypertension,heart_disease,ever_married,work_type,
                avg_glucose_level,smoking_status]).reshape(1,-1)

    scaler_path=os.path.join('/home/bhargav/College Project/Stroke_Prediction','scaler.pkl')
    scaler=None
    with open(scaler_path,'rb') as scaler_file:
        scaler=pickle.load(scaler_file)

    x=scaler.transform(x)

    model_path=os.path.join('/home/bhargav/College Project/Stroke_Prediction','trained_model.h5')
    dt= load_model(model_path)

    Y_pred=dt.predict(x, verbose=0)
    Y_pred=np.argmax(Y_pred, axis=-1)
    # for No Stroke Risk
    if Y_pred[0]==0:
        return HttpResponse("You Have No Risk Of Stroke")
    else:
        return HttpResponse("You have a risk of Stroke")