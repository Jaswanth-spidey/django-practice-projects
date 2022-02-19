from dataclasses import fields
from re import M, template
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
#importing CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from basic_app import models
from django.urls import reverse

# Create your views here.
#def index(request):
#    return render(request, 'index.html')

class Schoollist(ListView):
    #def get(self, request):
        #return HttpResponse("CLASS BASED VIEWS ARE COOL!!")

    #template_name = 'index.html'

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['injectme'] = 'BASIC INJECTION'
    #    return context
    model = models.School
    #it returns a list of name school_list -> as a context dictionary

class Schooldetailview(DetailView):
    #it returns just all lower cased as model -> School model as 'school' context dictionary
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    








