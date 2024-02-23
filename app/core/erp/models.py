from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length = 150, verbose_name = 'nombres', unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table            = 'tipo'
        ordering            = ['id']

class Category(models.Model):
    name = models.CharField(max_length = 150, verbose_name = 'nombres')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table            = 'categoria'
        ordering            = ['id']


class Employee(models.Model):
    categ         = models.ManyToManyField(Category)
    type          = models.ForeignKey(Type, on_delete = models.CASCADE)
    names         = models.CharField(max_length = 150, verbose_name = 'nombres')
    num_documento = models.CharField(max_length = 10, verbose_name = 'numero_documento', unique = True)
    date_joined   = models.DateField(default = datetime.now, verbose_name = 'fecha_registro')
    date_creation = models.DateTimeField(auto_now = True, verbose_name = 'fecha_creacion')
    date_updated  = models.DateTimeField(auto_now_add = True, verbose_name = 'fecha_creacion')
    age           = models.PositiveBigIntegerField(default = 0)
    salary        = models.DecimalField(default = 0.00, max_digits = 9, decimal_places = 2)
    state         = models.BooleanField(default = True)
    gender        = models.CharField(max_length = 50)
    avatar        = models.ImageField(upload_to = 'avatar/%y/%m/%d', null = True, blank = True)
    cvitae        = models.FileField(upload_to = 'cvitae/%y/%m/%d', null = True, blank = True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name        = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table            = 'empleado'
        ordering            = ['id']