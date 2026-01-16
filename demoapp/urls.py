
from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('frutables/<int:shop_id>',views.details,name='details'),
    path('add/',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]
