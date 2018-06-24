from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from sharedcare.views.allergy import *
from sharedcare.views.doctor import *
from sharedcare.views.food import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^allergies/$', allergy_list, name='allergy_list'),
    url(r'^allergies/create/$', allergy_create, name='allergy_create'),
    url(r'^allergies/(?P<pk>\d+)/update/$', allergy_update, name='allergy_update'),
    url(r'^allergies/(?P<pk>\d+)/delete/$', allergy_delete, name='allergy_delete'),
    url(r'^doctors/$', doctor_list, name='doctor_list'),
    url(r'^doctors/create/$', doctor_create, name='doctor_create'),
    url(r'^doctors/(?P<pk>\d+)/update/$', doctor_update, name='doctor_update'),
    url(r'^doctors/(?P<pk>\d+)/delete/$', doctor_delete, name='doctor_delete'),
    url(r'^foods/$', food_list, name='food_list'),
    url(r'^foods/create/$', food_create, name='food_create'),
    url(r'^foods/(?P<pk>\d+)/update/$', food_update, name='food_update'),
    url(r'^foods/(?P<pk>\d+)/delete/$', food_delete, name='food_delete'),
]

urlpatterns += staticfiles_urlpatterns()