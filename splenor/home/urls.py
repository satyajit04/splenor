from django.conf.urls import url, include
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/$', views.products_index, name='products_index'),
    #belt buckles
    url(r'^beltbuckles/$', views.beltbuckles_index, name='beltbuckles_index'),
    #zippers
    url(r'^zippers/$', views.zippers_index, name='zippers_index'),
    #laces
    url(r'^laces/$', views.laces_index, name='laces_index'),
    #waistbelts
    url(r'^waistbelts/$', views.waistbelts_index, name='waistbelts_index'),
    #sliders
    url(r'^sliders/$', views.sliders_index, name='sliders_index'),
    #buttons
    url(r'^buttons/bycategory/$', views.buttonsc_index, name='buttonsc_index'),
    url(r'^buttons/bystyle/$', views.buttonss_index, name='buttonss_index'),
]
