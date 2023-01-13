from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('', views.allprocat, name='allprocat'),
    path('<slug:cslug>/', views.allprocat, name='product_by_category'),
    path('<slug:cslug>/<slug:pslug>/', views.prodetail, name='prodetail'),
]
