from django.shortcuts import render
import SearchImage


def view(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'search.html', context)

def result(request):
    context          = {}
    result = SearchImage.search("images/001.jpg")
    context['result'] = result
    return render(request, 'search_result.html', context)