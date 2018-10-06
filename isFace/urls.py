from django.urls import path
from isFace import views

urlpatterns =[
    path('',views.isface,name='isface'),
]
