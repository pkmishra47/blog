from django.shortcuts import render
from django.http import HttpResponse

data = [
	{
		"username":"Pradeep Mishra",
		"description":"Hey guys! This is my first post. Hope you like it.",
		"date":"29th Sept, 2020"
	},
	{
		"username":"Abhinash Mishra",
		"description":"Sanatan Dharma hi karma hai",
		"date":"28th Sept, 2020"
	},
	{
		"username":"Deepak Mishra",
		"description":"My bussiness is my bussiness, none of your bussiness.",
		"date":"26th Sept, 2020"
	},		
]

def home(request):
	return render(request,'blog/test.html',{'posts':data})

# def about(request):
# 	return HttpResponse('<h1>Welcome to about page</h1>')	

