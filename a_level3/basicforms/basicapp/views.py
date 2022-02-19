from django.shortcuts import render
from . import forms
from basicapp.forms import FormName

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form_name_view(request):
    form_val_for_context = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            #DO something with the code will worjk
            print("Validation Successful")
            print("Name: "+form.cleaned_data["name"])
            print("Email: "+form.cleaned_data["email"])
            print("Text: "+form.cleaned_data["text"])

    return render(request, 'form_page.html',{'form_key':form_val_for_context})
