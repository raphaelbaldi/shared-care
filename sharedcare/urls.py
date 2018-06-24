from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from sharedcare.sharedcare import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^allergies/$', views.allergy_list, name='allergy_list'),
    url(r'^allergies/create/$', views.allergy_create, name='allergy_create'),
    url(r'^allergies/(?P<pk>\d+)/update/$', views.allergy_update, name='allergy_update'),
    url(r'^allergies/(?P<pk>\d+)/delete/$', views.allergy_delete, name='allergy_delete'),
    url(r'^doctors/$', views.doctor_list, name='doctor_list'),
    url(r'^doctors/create/$', views.doctor_create, name='doctor_create'),
    url(r'^doctors/(?P<pk>\d+)/update/$', views.doctor_update, name='doctor_update'),
    url(r'^doctors/(?P<pk>\d+)/delete/$', views.doctor_delete, name='doctor_delete'),
]

urlpatterns += staticfiles_urlpatterns()