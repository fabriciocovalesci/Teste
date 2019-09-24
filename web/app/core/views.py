from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django.core.files.storage import  FileSystemStorage
from .models import Foto

# Create your views here.

def home(request):
    conta = User.objects.count()
    return render(request, 'home.html',{
        'conta' : conta
    })

def registrar(request):
    if request.method == 'POST':    
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {
        'form' : form
    })

def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES['document']
        foto = FileSystemStorage()
        foto.save(upload_file.name, upload_file.file)
    return render(request, 'upload.html')

def exibir(request):
    if request.method == 'GET':
        foto_image = Foto.objects.all()
        return render(request, 'exibir.html', {'foto': foto_image})
  
