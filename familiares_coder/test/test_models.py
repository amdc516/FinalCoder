#import unittest
from django.test import TestCase

from familiares_coder.models import Mascota

class TestMascota(TestCase):
    def test_create_mascota(self):
        mascota = Mascota.objects.create(nombre='AbCd',edad='107',animal='xyz')
        
        assert isinstance (mascota, Mascota)
        assert mascota.nombre == 'AbCd'
        assert mascota.edad =='107'
        assert mascota.animal == 'xyz'
