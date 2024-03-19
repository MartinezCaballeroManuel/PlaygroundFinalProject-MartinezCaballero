from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth.models import User

from app import models

# Create your tests here.

class TestCaseBlog(TestCase):
    def setUp(self):
        # Creo un blog como ejemplo de pruebas
        self.blog = models.Blog.objects.create(titulo='Soy un titulo', subtitulo='Soy un subtitulo',cuerpo='Soy un cuerpo',autor='Soy un autor', fecha='Soy una fecha')
        # Defino las url a ser testeadas
        self.url_detail = reverse('detail', arg=[self.blog])
        self.url_delete = reverse('delete', arg=[self.blog])
        self.url_edit = reverse('edit', arg=[self.blog])
        
    # --Test 1-- Verifica que el código funcione correctamente al ejecutar la url 'detail'
    def test_detalle_blog(self):
        respuesta = self.client.get(self.url_detail)
        self.assertEqual(respuesta.status_code, 200)

    # --Test 2-- Verifica que la url 'edit' no reedirige al template 'edit.html' sino a 'pages.html'
    def test_editar_blog(self):
        respuesta = self.client.get(self.url_edit)
        self.asserTrue(self.assertTemplateNotUsed(respuesta, 'edit.html'))

    # --Test 3-- Verifica que la url 'delete' reedirige al template 'pages.html'
    def test_borrar_blog(self):
        respuesta = self.client.get(self.url_delete)
        self.assertTemplateUsed(respuesta, 'pages.html')
    