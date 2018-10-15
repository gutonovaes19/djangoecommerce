# coding=utf-8

from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
<<<<<<< HEAD
        # cria apenas para o teste
=======
        # cria apemas para o teste
>>>>>>> f0b2c9b122a050e33978d1496205ff46780e43a1
        self.client = Client()
        self.url = reverse('index')


    def tearDown(self):
<<<<<<< HEAD
        # remove o que tiver sido criado durante o teste
        pass

    def test_status_code(self):
        #se a view index esta retornando o codigo de resposa 200 (ok), 404 (nao encotnrado) 302 (redirecy)
=======
        # remove o que tiver sido criado
        pass

    def test_status_code(self):
>>>>>>> f0b2c9b122a050e33978d1496205ff46780e43a1
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)

    def test_template_used(self):

        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'index.html')


