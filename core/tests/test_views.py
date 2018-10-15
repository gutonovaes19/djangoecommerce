# coding=utf-8

from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        # cria apenas para o teste
        self.client = Client()
        self.url = reverse('index')


    def tearDown(self):
        # remove o que tiver sido criado durante o teste
        pass

    def test_status_code(self):
        #se a view index esta retornando o codigo de resposa 200 (ok), 404 (nao encotnrado) 302 (redirecy)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)

    def test_template_used(self):

        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'index.html')


