from django.urls import path
from .views import main_page, add_product_view

urlpatterns = [
    path('', main_page, name='home'),
    path('add_product/', add_product_view, name='add'),
]