from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('jokes.html', views.JokesList.as_view(), name='jokes'),
    path('poems.html', views.PoemsList.as_view(), name='poems'),
    path('test', views.test, name='test'),
]