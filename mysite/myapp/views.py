from django.shortcuts import render
from .models import Book

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("salut la famille")

def canon(request):
    return HttpResponse("str(request)")

def book_by_id(request,book_id):
     book = Book.objects.get(pk=book_id)
     return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")

def rend(request):
    return render(request,"main2.html")