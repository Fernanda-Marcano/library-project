from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, CreateView, DetailView, ListView

from .models import Author, Category, Book
from .forms import AuthorForm, CategoryForm, BookForm


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create.html'
    
    def get_context_data(self, **kwargs):
        #context = super(CLASS_NAME, self).get_context_data(**kwargs)
        context = {}
        context['authors'] = self.form_class
        context['aut'] = 'Crear Autor'
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list-author')


class AuthorListView(ListView):
    model = Author
    template_name = "author/list.html"
    
    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.model.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = 'Lista de Autores'
        context['authors'] = self.get_queryset()
        return context
