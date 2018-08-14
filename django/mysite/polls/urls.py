from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index")
    # path('show-index', views.index, name="index")
    path('show-index/from-poll', views.index, name="index")
]
