from django.shortcuts import render

def home(request):
    template_name = "halaman/base.html"
    context = {
        'title':'Selamat datang di website saya!',
        'umur': 20,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    context = {
        'title':'Ini biodata tentang saya',
        'umur': 20,
    }
    return render(request, template_name, context)