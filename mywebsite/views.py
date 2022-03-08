# This (views.py) file Created By Manually(Rahul).
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
        return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    djtext = request.POST.get('text', 'Defualt')
    removepunc = request.POST.get('removepunc', 'off')
    captiales = request.POST.get('captial', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')
    space_remove = request.POST.get('spaceremove', 'off')
    char_count = request.POST.get('charcounter', 'off')
    punctuations = '''!"#$%&'()*+,-./:;<=>?@£[\]^_`{|}~'''
    if removepunc == 'on' and captiales == 'on' and newlineremove == 'on' and space_remove == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        for char in analyzed:
            if char not in  punctuations:
                analyzed = analyzed + char
        for char in analyzed:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        for index, char in enumerate(analyzed):
            if not(analyzed[index] == ' ' and analyzed[index+1] == ' '):
                analyzed = analyzed + char            
        params= {'purpose':'Removed Punctuations, Change To Uppercase,Remove Newlines and Remove Extra Spaces', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and captiales == 'on':
        analyzed = ''
        for char in djtext:
            if char not in  punctuations:
                analyzed = analyzed + char.upper()
        params= {'purpose':'Removed Punctuations With Change To Uppercase', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and newlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char not in  punctuations:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
        params= {'purpose':'Removed Punctuations With Remove Newlines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif removepunc == 'on' and space_remove == 'on':
        analyzed = ''
        for char in djtext:
            if char not in  punctuations:
                analyzed = analyzed + char
        for index, char in enumerate(analyzed):
            if not(analyzed[index] == ' ' and analyzed[index+1] == ' '):
                analyzed = analyzed + char
        params= {'purpose':'Removed Punctuations With Remove extra Spaces', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif space_remove == 'on' and newlineremove == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
            for char in analyzed:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
        params= {'purpose':'Remove Extra Spaces with Remove Newlines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif space_remove == 'on' and captiales == 'on':
        analyzed = ''
        for index,char in enumerate(djtext):
                if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                    analyzed = analyzed + char.upper()
                
        params= {'purpose':'Remove Extra Spaces with Change To Uppercase', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif captiales == 'on' and newlineremove == 'on':
        analyzed = ''
        for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char.upper()
        params= {'purpose':'Change To Uppercase With Remove Newlines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    

    elif removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@£[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in  punctuations:
                analyzed = analyzed + char
        params= {'purpose':'Removed Punctuations', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif captiales == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params= {'purpose':'Change To Uppercase', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params= {'purpose':'Remove Newlines', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif space_remove == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char

        params= {'purpose':'Remove Extra Spaces', 'analyze_text': analyzed}
        return render(request, 'analyze.html', params)
    elif char_count == 'on':
        count = 0
        for index in djtext:
            count = count+1

        params= {'purpose':'Char counter', 'analyze_text': f"Your Words Char Count is: {count}"}
        return render(request, 'analyze.html', params)
    else:
        params= {'purpose':'Removed Punctuations', 'analyze_text': djtext}
        return HttpResponse("Error!!!")
