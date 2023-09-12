# I have creater this file  
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'Sagar','place':'mars'}
    return render(request,'index2.html',params)
    # return HttpResponse("hellloo bhai")

def about(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    toupper=request.GET.get('toupp','off')
    newline=request.GET.get('newlineremover','off')
    extraspce=request.GET.get('extraspace','off')
    toggle=request.GET.get('toggle','off')
    # print(removepunc)
    # print(djjtext)
    # print(djtext)
    analyzer=""
    if removepunc=="on" and toupper=='on':
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzer=analyzer+char.upper()
        params={'analz':analyzer,'regular':'punctuations'}
        return render(request,'index2.html',params)


    elif removepunc=="on":
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzer=analyzer+char
        params={'analz':analyzer,'regular':'punctuations'}
        return render(request,'index2.html',params)
    elif toupper=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'analyzed':analyzed,'regular':'toupp'}
        return render(request,'index2.html',params)
    elif newline=='on':
        remove=''
        for char in djtext:
            if char!="\n":
                remove=remove+char
        params={'remove':remove,'regular':'lineremover'}
        return render(request,'index2.html',params)
    elif extraspce=='on':
        removee=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                removee=removee+char
        params={'removee':removee,'regular':'extraspace'}
        return render(request,'index2.html',params)
    elif toggle=='on':
        word=''
        for char in djtext:
            if char>='a' and char<='z':
                word=word+char.upper()
            else:
                word=word+char.lower()
        params={'word':word,'regular':'toggle'}
        return render(request,'index2.html',params)
    else:
        return HttpResponse("Error")
    # return HttpResponse("Sagar Bhai")