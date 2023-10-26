from django.shortcuts import render
from . forms import KontakForm

# Create your views here.

def kontak_view(request):
    if request.method=='POST':
        form = KontakForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = KontakForm()
        return render(request, 'kontak_form.html', { 'form': form })