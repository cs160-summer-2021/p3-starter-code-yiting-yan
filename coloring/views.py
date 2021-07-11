from django.shortcuts import render


def index(request):
    return render(request, 'coloring/index.html')


def palette(request):
    return render(request, 'coloring/palette.html')


def palette2(request):
    return render(request, 'coloring/palette2.html')


def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')
