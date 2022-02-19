from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content',"Hello Im from models_app"}
    return render(request, 'index.html',context=my_dict)
