from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
	return HttpResponse("Welcome django Page")

def about(request):
	return HttpResponse("<h2 style='background-color:green'> hello</h2>")

def rc(y,name):
	return HttpResponse("<h2>Hii Welcome{}</h2>".format(name))
def tb(n1,n):
	k=" "
	for i in range(1,11):
		k+="{} * {} = {}".format(n,i,n*i)+"<br/>"
	print(k)
	return HttpResponse(k)

def rcds(request,name,age):
	#print(name,age)
	return render(request,"samples.html",{'name':name,'age':age})

def sample(request):
	return render(request,'cssdemo.html')


def login(request):
	return render(request,'login.html')

def register(request):
	return render(request,'register.html')