from django.shortcuts import render

# Create your views here.


def song(request):
    context = {
        'title': 'Mi primera pagina',
        "content": "Cuerpo de la página"
    }
    return render(request, 'Music/song.html', context)
