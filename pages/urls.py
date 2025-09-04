from django.urls import path
from pages import views
from .views import home_view

urlpatterns = [
    path('', home_view, name="home"),
]


