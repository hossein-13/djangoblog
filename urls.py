
from django.urls import path
from . import views

app_name = "balhbalh"
urlpatterns = [
    path('', views.articles_list, name="list"),
    path('create', views.create_list, name="create"),
    path('<slug>', views.articles_detail, name="detail"),
]
