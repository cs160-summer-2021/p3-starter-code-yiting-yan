from django.shortcuts import render


def index(request):
    return render(request, 'coloring/index.html')


def demo(request):
    return render(request, 'coloring/demo.html')


def palette(request):
    return render(request, 'coloring/palette.html')


def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')
