from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DetailView, ListView, UpdateView

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


class CategoryView(View):
    model = Category
    form_class = CategoryForm
    template_name = 'category/categories.html'
    
    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = {}
        context['categories'] = self.get_queryset()
        context['form_category'] = self.form_class
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list-category')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book/create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        context['title'] = 'Crear Libro'
        context['c_book'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list-book')


class BookListView(ListView):
    model = Book
    template_name = "book/list.html"
    
    def get_queryset(self):
        query = self.model.objects.all()
        return query
    
    def get_context_data(self, **kwargs):
        context = {}
        context['books'] = self.get_queryset()
        context['l_books'] = 'Lista de Libros'
        return context


class BookUpdateView(UpdateView):
    model = Book
    template_name = "book/create.html"
    form_class = BookForm
    success_url = reverse_lazy('list-book')
    
    def get_context_data(self, **kwargs):
        context = {}
        context['title'] = 'Actualizar Libro'
        context['c_book'] = self.get_form()
        return context