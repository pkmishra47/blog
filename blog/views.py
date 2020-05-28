from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Members

def home(request):
	members = Members.objects.all()
	members_data = []
	gallery_data = []

	for member in members:
		members_data.append({"name":member.name,"description":member.description,"image_name":member.image_name})
		gallery_data.append({"image_name":member.image_name})
		
	return render(request,'blog/test.html',{'members_data':members_data,"gallery_data":gallery_data})

def test(request):
	members = Members.objects.all()
	members_data = []
	
	for member in members:
		members_data.append({"name":member.name,"description":member.description,"image_name":member.image_name})
	print("members:{}".format(members))
	return render(request,'blog/base.html',{'members_data':members_data})	

# def about(request):
# 	return HttpResponse('<h1>Welcome to about page</h1>')	

