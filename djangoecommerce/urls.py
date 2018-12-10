"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#struing de regex - ignora alguns caracteres. O Circuflexo indica inicio da string - estudar expressoes regulares
                # cifrão indica fim da url.
from django.conf.urls import url
from django.contrib import admin

from core.views import index
# struing de regex - ignora alguns caracteres. O Circuflexo indica inicio da string - estudar expressoes regulares
# cifrão indica fim da url.
from django.conf.urls import url, include
from django.contrib import admin

from core import views
from catalog import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^produto/$', views.product, name='product'),
    url(r'^produtos/$', includr('catalog.urls', namespace = 'catalog')),
    url(r'^admin/', admin.site.urls),
]
