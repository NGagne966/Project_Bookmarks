from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the Bookmarks index.")
    #return render(request, 'bookmarks_list.html', {})
    return render(request, 'index.html', {})