from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arborescence', views.index_arborescence),
    path('FAQ', views.index_FAQ)
]