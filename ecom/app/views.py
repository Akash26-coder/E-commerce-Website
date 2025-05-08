from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def addtocart(request):
    return render(request,'addtocart.html')

def payment(request):
    return render(request,'payment.html')
