# Generated by Django 5.1.2 on 2024-10-16 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Autor')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Biografía')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'Autor',
                'ordering': ['id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre de Categoría')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'Categoría',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Título del Libro')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('pub_year', models.DateField(verbose_name='Fecha de Publicación')),
                ('image', models.ImageField(default='image/fondo.png', upload_to='image/', verbose_name='Imagen')),
                ('file', models.FileField(blank=True, null=True, upload_to='books/', verbose_name='Libro')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='library_app.author', verbose_name='Autor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'db_table': 'Libro',
                'ordering': ['title'],
            },
        ),
    ]