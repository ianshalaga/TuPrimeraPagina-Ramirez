from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'title': 'Mi primera pagina'}
    return render(request, 'MyApp/index.html', context=context)
