from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('shop', views.shop,name='shop'),
    path('<slug:c_slug>/',views.shop,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.detail,name='detail'),
    path('search',views.searching,name='search'),
]
