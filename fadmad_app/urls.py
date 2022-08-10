from django.urls import path
from fadmad_app import views

urlpatterns = [
    path('',views.contact, name='contact'),
]
