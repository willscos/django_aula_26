from django.urls import path
from .views import home
from .views import *


urlpatterns = [
    path('', home),
    path('criar/', criar),
    path('editar/<int:id>/', editar),
    path('deletar/<int:id>/', deletar),
]