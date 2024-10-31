from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.AuthorCreate.as_view(), name='create-author'),
    path('list/', views.AuthorListView.as_view(), name='list-author'),
    path('category-list/', views.CategoryView.as_view(), name='list-category'),
]
