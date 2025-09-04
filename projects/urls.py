from django.urls import path
from projects import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path("project_index/", views.project_index, name="project_index"),
    path("project_detail/<int:pk>/", views.project_detail, name="project_detail"),
    path("create/", views.create_project_view, name="create_project_view"),
    path("login/", LoginView.as_view(template_name="projects/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_user, name="register_user"),
    path("delete/<int:pk>/", views.delete_project, name="delete_project"),
]