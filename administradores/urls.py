from django.urls import path
from .views import login, Ventas_panel_Admin

urlpatterns = [
    path('login/', login, name='login'),
    path('ventas/', Ventas_panel_Admin, name='ventas'),
]
