from django.urls import path
from .import views

urlpatterns = [

    # store main
    path('', views.store, name='store'),

    # individual products
    path('product/<slug:product_slug>/',
         views.product_info, name='product_info'),

    # individual catergories
    path('search/<slug:category_slug>/',
         views.list_category, name='list-category'),
]
