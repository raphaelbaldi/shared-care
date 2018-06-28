from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from sharedcare.views.allergy import *
from sharedcare.views.doctor import *
from sharedcare.views.elderly import *
from sharedcare.views.food import *
from sharedcare.views.medicine import *
from sharedcare.views.user_account import *

from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),

    url(r'^allergies/$', allergy_list, name='allergy_list'),
    url(r'^allergies/create/$', allergy_create, name='allergy_create'),
    url(r'^allergies/(?P<pk>\d+)/update/$', allergy_update, name='allergy_update'),
    url(r'^allergies/(?P<pk>\d+)/delete/$', allergy_delete, name='allergy_delete'),

    url(r'^doctors/$', doctor_list, name='doctor_list'),
    url(r'^doctors/create/$', doctor_create, name='doctor_create'),
    url(r'^doctors/(?P<pk>\d+)/update/$', doctor_update, name='doctor_update'),
    url(r'^doctors/(?P<pk>\d+)/delete/$', doctor_delete, name='doctor_delete'),

    url(r'^elderlies/$', elderly_list, name='elderly_list'),
    url(r'^elderlies/create/$', elderly_create, name='elderly_create'),
    url(r'^elderlies/(?P<pk>\d+)/update/$', elderly_update, name='elderly_update'),
    url(r'^elderlies/(?P<pk>\d+)/delete/$', elderly_delete, name='elderly_delete'),
    url(r'^elderlies/(?P<pk>\d+)/details/$', elderly_details, name='elderly_details'),
    url(r'^elderlies/(?P<pk>\d+)/add_allergy/$', elderly_add_allergy, name='elderly_add_allergy'),
    url(r'^elderlies/(?P<pk>\d+)/delete_allergy/(?P<apk>\d+)/', elderly_delete_allergy, name='elderly_delete_allergy'),
    url(r'^elderlies/(?P<pk>\d+)/add_meal/$', elderly_add_meal, name='elderly_add_meal'),
    url(r'^elderlies/(?P<pk>\d+)/delete_meal/(?P<mpk>\d+)/', elderly_delete_meal, name='elderly_delete_meal'),
    url(r'^elderlies/(?P<pk>\d+)/add_medicine/$', elderly_add_medicine, name='elderly_add_medicine'),
    url(r'^elderlies/(?P<pk>\d+)/delete_medicine/(?P<mpk>\d+)/', elderly_delete_medicine, name='elderly_delete_medicine'),
    url(r'^elderlies/(?P<pk>\d+)/add_prescription/$', elderly_add_prescription, name='elderly_add_prescription'),
    url(r'^elderlies/(?P<pk>\d+)/delete_prescription/(?P<ppk>\d+)/', elderly_delete_prescription,
        name='elderly_delete_prescription'),
    url(r'^elderlies/(?P<pk>\d+)/add_medical_appointment/$', elderly_add_medical_appointment,
        name='elderly_add_medical_appointment'),
    url(r'^elderlies/(?P<pk>\d+)/delete_medical_appointment/(?P<mapk>\d+)/', elderly_delete_medical_appointment,
        name='elderly_delete_medical_appointment'),

    url(r'^foods/$', food_list, name='food_list'),
    url(r'^foods/create/$', food_create, name='food_create'),
    url(r'^foods/(?P<pk>\d+)/update/$', food_update, name='food_update'),
    url(r'^foods/(?P<pk>\d+)/delete/$', food_delete, name='food_delete'),

    url(r'^medicines/$', medicine_list, name='medicine_list'),
    url(r'^medicines/create/$', medicine_create, name='medicine_create'),
    url(r'^medicines/(?P<pk>\d+)/update/$', medicine_update, name='medicine_update'),
    url(r'^medicines/(?P<pk>\d+)/delete/$', medicine_delete, name='medicine_delete'),
]

urlpatterns += staticfiles_urlpatterns()
