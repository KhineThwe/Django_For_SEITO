from django.shortcuts import render
import pymongo

connection = pymongo.MongoClient("localhost",27017)
database = connection["djDB"]
collection = database["djCO"]
data = collection.find_one()

def home(request):
    try:
        return render(request,'home.html',{'data':data})
        #object ကြီးတစ်ခုလုံးပေးလိုက်မယ်
    except Exception as error:
        print(error)
        return render(request,'home.html',{'error':error})

def about(request):
   try:
        return render(request,'about.html',{'data':data})
        #object ကြီးတစ်ခုလုံးပေးလိုက်မယ်
   except Exception as error:
        print(error)
        return render(request,'about.html',{'error':error})

def add(request):
    uname = request.POST['name'] 
    uemail = request.POST['email'] 
    upass = request.POST['password']
    return render(request,'result.html',{'name':uname,'email':uemail,'password':upass})