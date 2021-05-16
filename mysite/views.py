# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name': 'Aishwarya', 'place': 'mars'}
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About Aishwarya")


def navigation(request):
    s = '''<h1>Youtube</h1>  <br>  <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list
    =PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django documentation</a> <br>
    <a href = "https://docs.djangoproject.com/en/3.2/intro/tutorial01/>Django</a>"'''

    return HttpResponse(s)


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)



    elif fullcaps == "on":

        analyzed = ""

        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed = ""

        params = {'purpose': 'count', 'analyzed_text': analyzed}

        # Analyze the text

        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        analyzed = len(djtext)

        params = {'purpose': 'character count', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)


    else:

        return HttpResponse('Error')


def Capitalize(request):
    return HttpResponse("RMove capitalize ")


def spaceremove(request):
    return HttpResponse('''RMove capitalize <a href ="http://127.0.0.1:8000/Capitalize ">back</a>''')
