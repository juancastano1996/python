from django.test import TestCase
from app.wsgi import *
from core.erp.models import Type

#Listar
#query = Type.objects.all()
#print(query)

#Insertar
#t = Type()
#t.name = 'Prueba'
#t.save()

#Editar
#try:
#    t = Type.objects.get(id = 2)
#    t.name = 'Prueba'
#    t.save()
#    #print(t.name)
#except Exception as e:
#    print(e)

#Eliminar
#t = Type.objects.get(pk = 1)
#t.delete()
#print(query)


for i in Type.objects.filter(name__endswith = 'a'):
    print(i.name)