from django.urls import path
from loginApp.views import *

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("api/login/", UsuariosDetails.as_view()),
]