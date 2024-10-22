from django import forms
from .models import Author, Category, Book


class AuthorForm(forms.ModelForm):
    """Form definition for Author."""

    class Meta:
        """Meta definition for Authorform."""

        model = Author
        fields = ['id','name', 'last_name', 'biography']
        labels = {
            'name':'Nombre',
            'last_name':'Apellido',
            'biography':'Biografía'
        }
        """ widgets = {
            'name':forms.TextInput(attrs={})
        } """


class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = '__all__'
        labels = {
            'name':'Nombre de la Categoría'
        }


class BookForm(forms.ModelForm):
    """Form definition for Book."""
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None, label='Autor', required=True, widget=forms.Select(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, label='Categoría', required=True, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        """Meta definition for Bookform."""

        model = Book
        fields = ['title','description', 'pub_year', 'image', 'file', 'author', 'category']
        labels = {
            'title':'Título', 
            'description':'Descripción', 
            'pub_year':'Fecha de Publicación',
            'image':'Imagen', 
            'file':'Archivo'
        }
