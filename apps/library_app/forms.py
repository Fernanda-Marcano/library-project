from django import forms
from .models import Author, Category, Book


class AuthorForm(forms.ModelForm):
    """Form definition for Author."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

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
            'name':forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}), 
            'last_name':forms.TextInput(attrs={'class':'form-control', 'autocomplete':'off'}),
            'biography':forms.Textarea(attrs={'class':'form-control', 'autocomplete':'off'}),
        } """


class CategoryForm(forms.ModelForm):
    """Form definition for Category."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = '__all__'
        labels = {
            'name':'Nombre de la Categoría'
        }


class BookForm(forms.ModelForm):
    """Form definition for Book."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            if form.field.widget == 'FileInput':
                form.field.widget.attrs['class'] = 'form-control-file'
    
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None, label='Autor', required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, label='Categoría', required=True)

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
