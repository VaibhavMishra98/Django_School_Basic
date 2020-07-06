from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models
from django.http import HttpResponse
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "Check the list of Schools!!"
        return context

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'mind/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("mind:list")
