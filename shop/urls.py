from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('shop', views.shop,name='shop'),
    path('<slug:c_slug>/',views.shop,name='prod_cat'),
    path('detail', views.detail,name='detail'),
]
