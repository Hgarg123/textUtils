from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'harshit Garg', 'place': 'India'}
    return render(request, 'textUtlisBootstrap.html', params)


# request.GET.get('text','default') will shows that method is get and print the text having name='text' on terminal

def textAnalze(request):
    print(request.POST.get('text', 'default'))
    return HttpResponse("hello")


def removepunch(request):
    djtext = request.POST.get('text', 'default')
    print(djtext)
    checkstatuspunch = request.POST.get('checkbox', 'default')
    print(checkstatuspunch)
    checkstatuscapital = request.POST.get('capital', 'default')
    remove = ""
    punctuation = '''!()-[]{};:'"\, <>./=?@#$%^&*_~'''
    if checkstatuspunch == 'on':
        for i in djtext:
            if i not in punctuation:
                remove = remove + i
    elif checkstatuscapital == 'on':
        for i in djtext:
            remove = remove + i.upper()

    else:
        return HttpResponse("error")

    param = {'purpose': remove, 'analyes_text': checkstatuspunch}
    return render(request, 'Analze.html', param)
