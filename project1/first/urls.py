from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path("",views.index,name='Home'),
    path("addemp",views.addemp, name='addemp'),
    path("updateemp/<int:id>",views.updateemp,name='updateemp'),
    path("deleteemp/<int:id>",views.deleteemp,name='deleteemp'),
    path("adddept",views.adddept,name='adddept'),
    path("deletedept/<int:id>",views.deletedept,name='deletedept'),
    path("updatedept/<int:id>",views.updatedept,name='updatedept'),
]