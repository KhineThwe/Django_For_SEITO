from django.shortcuts import render
import pymongo

connection = pymongo.MongoClient("localhost",27017)
database = connection["djDB"]
collection = database["djCO"]

def home(request):
    try:
        data = collection.find_one()
        for doc in data.items():
            print(doc)
        id,name,age,hobby = data['_id'],data['name'],data['age'],data['hobby']
        return render(request,'home.html',{'id':id,'name':name,'age':age,'hobby':hobby})
    except Exception as error:
        print(error)
        return render(request,'home.html',{'error':error})

def about(request):
    return render(request,'about.html',{'data':'Django Learning'})