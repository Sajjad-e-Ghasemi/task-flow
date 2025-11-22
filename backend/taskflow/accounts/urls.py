from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.AccountView.as_view(), name='account'),
]
