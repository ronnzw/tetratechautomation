from . import views
from django.urls import path

app_name = "tetautoapp"
urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path('ourServices',views.ourServices,name="ourServices"),
    path('cliental',views.cliental,name="cliental"),
    path('contact',views.contact_view,name="contact"),
    path('success',views.success,name="success"),
]