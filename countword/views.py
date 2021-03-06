from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    text_list = fulltext.split()
    dictionary={}
    for x in text_list:
        dictionary[x]=text_list.count(x)
    dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'total':len(text_list), 'dictionary':dictionary})


