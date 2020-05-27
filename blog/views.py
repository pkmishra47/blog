from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Members

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
	members = Members.objects.all()
	members_data = []

	for member in members:
		members_data.append({"name":member.name,"description":member.description,"image_name":member.image_name})
	print("members:{}".format(members_data))
	return render(request,'blog/test.html',{'members_data':members_data})

def test(request):
	members = Members.objects.all()
	members_data = []
	
	for member in members:
		members_data.append({"name":member.name,"description":member.description,"image_name":member.image_name})
	print("members:{}".format(members))
	return render(request,'blog/base.html',{'members_data':members_data})	

# def about(request):
# 	return HttpResponse('<h1>Welcome to about page</h1>')	

