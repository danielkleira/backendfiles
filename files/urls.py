from django.urls import path

from . import views

urlpatterns = [
    path("file/", views.UpFile.as_view()),
    path("file/list", views.FileView.as_view()),
]
