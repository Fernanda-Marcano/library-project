from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.AuthorCreate.as_view(), name='create-user'),
    path('list/', views.AuthorListView.as_view(), name='list-author'),
]
