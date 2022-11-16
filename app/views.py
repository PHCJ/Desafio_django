from django.shortcuts import render
'''from django.http import HttpResponse
def teste(request):
    return HttpResponse('teste ok')'''

def home(request):
    return render(request, 'app/index.html')
