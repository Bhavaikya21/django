from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('fact/<n>', views.fact, name="fact"),
    path('child/', views.child, name="child"),
]
