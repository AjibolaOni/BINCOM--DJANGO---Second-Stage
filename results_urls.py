from django.urls import path
from . import views

urlpatterns = [
    path('polling_unit/<int:uniqueid>/', views.polling_unit_results, name='polling_unit_results'),
    path('lga_results/', views.lga_results, name='lga_results'),
    path('new_polling_unit/', views.new_polling_unit, name='new_polling_unit'),
]