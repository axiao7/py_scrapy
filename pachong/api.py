from django.http import JsonResponse
import json

def info(request):
    f = open('../info.txt', encoding='utf-8')
    content = f.read()
    f.close()
    content = eval(content)
    return JsonResponse(content, safe=False)