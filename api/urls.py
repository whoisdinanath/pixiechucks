from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.InputCreate.as_view(), name='input'),
    path('output/', views.OutputList.as_view(), name='output')


]
