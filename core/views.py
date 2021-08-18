from django.shortcuts import render, HttpResponse, redirect

def inicio(request):
    # cargo mil cosas de la base datos. 
    return redirect("/show_index")

def index(request):
    context = {
        'usuario': 'Francisco'
    }
    return render(request, 'index.html', context)

def libro(request):
    context = {
        'usuario': 'Pancho'
    }
    return render(request, 'libro.html', context)

def autor(request):
    context = {
        'usuario': 'Javier'
    }
    return render(request, 'autor.html', context)

def ninja(request):
    context = {
        'usuario': 'Boisier'
    }
    return render(request, 'ninja.html', context)