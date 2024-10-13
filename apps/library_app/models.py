from django.db import models


class Author(models.Model):
    """Model definition for Autor."""
    name = models.CharField(verbose_name='Nombre del Autor', max_length=100, null=False, blank=False)
    last_name = models.CharField(verbose_name='Apellido', max_length=100, null=False, blank=False)
    biography = models.TextField(verbose_name='Biografía', null=True, blank=True)

    class Meta:
        """Meta definition for Autor."""
        db_table = 'Autor'
        ordering = ['id', 'name']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        """Unicode representation of Autor."""
        return f'{self.name} {self.last_name}'
    
    def clean(self):
        if self.name:
            self.name = self.name.capitalize().strip()
        if self.last_name:
            self.last_name = self.last_name.capitalize().strip()
        if self.biography:
            self.biography = self.biography.strip()


class Category(models.Model):
    """Model definition for Category."""
    name = models.CharField(verbose_name='Nombre de Categoría', max_length=100, null=False, blank=False, unique=True)

    class Meta:
        """Meta definition for Category."""
        db_table = 'Categoría'
        ordering = ['name']
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name
    
    def clean(self):
        if self.name:
            self.name = self.name.title().strip()


class Book(models.Model):
    """Model definition for Book."""
    title = models.CharField(verbose_name='Título del Libro', max_length=200, null=False, blank=False, unique=True)
    description = models.TextField(verbose_name='Descripción', null=False, blank=False)
    pub_year = models.DateField(verbose_name='Fecha de Publicación', null=False, blank=False)
    image = models.ImageField(verbose_name='Imagen', upload_to='image/', default='image/fondo.png')
    file = models.FileField(verbose_name='Libro', upload_to='books/', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, verbose_name='Autor')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='Categoría', null=True)

    class Meta:
        """Meta definition for Book."""
        db_table = 'Libro'
        ordering = ['title']
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        """Unicode representation of Book."""
        return f'{self.title}'
    
    def clean(self):
        if self.title:
            self.title = self.title.title().strip()
        if self.description:
            self.description = self.description.strip()
