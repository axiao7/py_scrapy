# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
 
def hello(request):
    f = open('../info.txt', encoding='utf-8')
    content = f.read()
    f.close()
    content = eval(content)
    context          = {}
    context['infos'] = content
    return render(request, 'index.html', context)