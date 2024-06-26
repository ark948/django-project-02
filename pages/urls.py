from django.urls import path
from pages import views

urlpatterns = [
    path("about/", views.AboutViewPage.as_view(), name="about"),
    path("", views.HomePageView.as_view(), name="home"),
]