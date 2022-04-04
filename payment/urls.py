from django.urls import path
from . import views



urlpatterns=[
    path('',views.subash,name='checkout'),

    # path('',views.checkout),

    path('success',views.success,name='success')
]