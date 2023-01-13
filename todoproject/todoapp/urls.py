from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('details',views.details, name='details')
    path('delete/<int:id>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('tlv/',views.tlv.as_view(),name='tlv'),
    path('tdv/<int:pk>/',views.tdv.as_view(),name='tdv'),
    path('tuv/<int:pk>/',views.tuv.as_view(),name='tuv'),
    path('tdel/<int:pk>/',views.tdel.as_view(),name='tdel'),
]
