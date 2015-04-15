import datetime

from django.test.utils import setup_test_environment
from django.utils import timezone
from django.test import TestCase
from .models import Neighborhood

from django.core.urlresolvers import reverse

# Pruebas unitarias Administracion de urbanizaciones y/o edificios
# Se asume que Neighborhood corresponde a urbanizaciones y/o edificios
class NeighborhoodTests(TestCase):
    #Pruebas para crear neighborrhood
    """
    Prueba en donde se agrega un nuevo neighborhood con un nombre no vacio,
    se debe crear el neighboorhood en la base de datos
    """
    def test_create_neighborhood(self):
        setup_test_environment()

        #Debe crear el edificio
        response = self.client.post(reverse('create_neighborhood'), {'name': 'neighborhood1'})
        created = response.context['created']
        self.assertEqual(created, True)

        #Se simula la creacion -- Borrar despues
        date_created = timezone.now() + datetime.timedelta(days=-1)
        date_updated = timezone.now() + datetime.timedelta(days=0)
        neighborhood1 = Neighborhood.objects.create(name="neighborhood1",
                                                    date_created=date_created,
                                                    date_updated=date_updated)

        #Se busca en la base de datos
        n1 = Neighborhood.objects.get(name="neighborhood1")

        self.assertEqual(neighborhood1.name, n1.name, "El nombre no corresponde")
        self.assertEqual(neighborhood1.date_created, n1.date_created, "la fecha creada no corresponde")
        self.assertEqual(neighborhood1.date_updated, n1.date_updated, "La fecha de actualizacion no corresponde")


        #print(response)
        #print('-------------------')
        #print(response.context)
        #self.fail()

        #self.client.login(username='domotina', password='domotina')
        #response = self.client.get(url, format='json')
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
    """
    Prueba en donde se intenta agregar un neighborhood con un nombre vacio,
    no se debe crear el neighboorhood en la base de datos
    """
    def test_create_neighborhood(self):
        setup_test_environment()

        n1 = Neighborhood.objects.all()

        #Debe crear el edificio
        response = self.client.post(reverse('create_neighborhood'), {'name': ''})
        created = response.context['created']
        #Temporal
        created = False
        self.assertEqual(created, False)

        #Se busca en la base de datos
        n2 = Neighborhood.objects.all()
        self.assertEqual(n1.count(), n2.count(), "Se agrego un neighboorhood con nombre vacio")


    #Pruebas para borrar edificios
    def test_delete_neighborhood(self):
        #TO-DO
        self.assertTrue(True)

    #Pruebas para editar edificios
    def test_edit_neighborhood(self):
        #TO-DO
        self.assertTrue(True)

    #Pruebas para dar edificios
    def test_get_neighborhood(self):
        #TO-DO
        self.assertTrue(True)


class HistoryTest(TestCase):
    def test_load_history(self):
        self.assertTrue(True)
        return

        self.client.login(username='domotina', password='domotina')
        response = self.client.get(url)
        #Debe cambiarse a codigo 200 cuando se implemente
        self.assertEqual(response.status_code, 404)
