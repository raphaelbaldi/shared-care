from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sharedcare.sharedcare import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^allergies/$', views.allergy_list, name='allergy_list'),
    url(r'^allergies/create/$', views.allergy_create, name='allergy_create'),
    url(r'^allergies/(?P<pk>\d+)/update/$', views.allergy_update, name='allergy_update'),
    url(r'^allergies/(?P<pk>\d+)/delete/$', views.allergy_delete, name='allergy_delete'),
]

urlpatterns += staticfiles_urlpatterns()