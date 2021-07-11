from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def palette(request):
    return render(request, 'coloring/palette.html')