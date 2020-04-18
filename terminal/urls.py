from django.urls import path

from . import views

urlpatterns = [
    path('', views.RequestView.as_view(), name='RequestView'),
    path('potato', views.potato, name='potato')
]
