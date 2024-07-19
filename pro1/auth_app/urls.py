from django.urls import path
from .views import *

urlpatterns = [
    path("suv/",signup_view),
    path("lv/",login_view),
    path("lo/",logout_view)
]