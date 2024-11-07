from django.urls import path
from . import views

urlpatterns = [
    #               URLs AUTHOR
    path('create-author/', views.AuthorCreate.as_view(), name='create-author'),
    path('list-author/', views.AuthorListView.as_view(), name='list-author'),
    
    #               URLs CATEGORY
    path('category-list/', views.CategoryView.as_view(), name='list-category'),
    
    #               URLs BOOK
    path('create-book', views.BookCreateView.as_view(), name='create-book'), 
    path('list-book', views.BookListView.as_view(), name='list-book'), 
    path('update-book/<int:pk>/', views.BookUpdateView.as_view(), name='update-book')
]
