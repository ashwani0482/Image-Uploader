from django.shortcuts import render
from .models import Image
from .forms import ImageForm

def home(request):
    
    if request.method=='POST':
        
      form = ImageForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         msg = "saved"

    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'form': form, 'img':img})
    