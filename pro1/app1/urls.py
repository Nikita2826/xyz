from django.urls import path
from .views import *

urlpatterns = [
    path("av/",add_view),
    path("sv/",show_view),
    path("uv/<int:pk>/",update_view),
    path("dv/<int:pk>/",delete_view)
]
