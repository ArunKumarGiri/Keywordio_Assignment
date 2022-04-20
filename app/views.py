from http.client import HTTPResponse
from itertools import product
from unicodedata import category
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import BookForm
# from django.db.models import Q
# from django.http import JsonResponse

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):       
        return render(request, 'app/home.html')

def profile(request):
    if request.method == "GET":   ##     get all the data means READ
        book=Book.objects.all()
        d1={"book":book}
        return render(request, 'app/profile.html',context=d1)

    elif request.method == "POST":  
        if 'btncreate' in request.POST:
            book=Book()
            book.name=request.POST.get("txtname","NA")     ### post data means CREATE
            book.writter=request.POST.get("txtwritter","NA")
            book.tittle=request.POST.get("txttittle","NA")
            book.publisher=request.POST.get("txtpublisher","NA")
            book.save()
            return HttpResponse("<h1> COUTOMER ADDED Successfully</h1>")

        elif 'btnupdate' in request.POST:
            book=Book()
            book_id=int(request.POST.get("txtid",0))
            if Book.objects.filter(id=book_id).exits():
                book.name=request.POST.get("txtname","NA")     ### update data means UPDATE
                book.writter=request.POST.get("txtwritter","NA")
                book.tittle=request.POST.get("txttittle","NA")
                book.publisher=request.POST.get("txtpublisher","NA")
                book.save()
                return HttpResponse("<h1> COUTOMER updated Successfully</h1>")


        elif 'btndelete' in request.POST:
            book_id=int(request.POST.get("txtid",0))
            Book.objects.get(id=book_id).delete()
            return HttpResponse("<h1> COUTOMER deleted Successfully</h1>")


def login(request):
 return render(request, 'app/login.html')

class customerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})

    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation! Registerd Successfully!!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})

