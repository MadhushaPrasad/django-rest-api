from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.get_all_projects),
    path('product/<id>', views.get_product_detail)
]
