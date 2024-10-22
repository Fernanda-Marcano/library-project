from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, ListView

from .models import Author, Category, Book
from .forms import AuthorForm, CategoryForm, BookForm


""" class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    context_object_name = 'autores'
    template_name = 'author/create.html' """




