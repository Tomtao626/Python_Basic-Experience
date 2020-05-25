from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def book(request):
    return HttpResponse("图书首页")

def book_detail(request,book_id,category_id):
    text = "你获取的图书id是：%s,你的图书分类id是：%s" % (book_id,category_id)
    return HttpResponse(text)