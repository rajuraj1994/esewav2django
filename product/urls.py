from django.urls import path
from .views import *


urlpatterns=[
    path('',index),
    path('addproduct/',post_product),
    path('addcategory/',post_category),
    path('showcategory/',show_category),
    path('deletecategory/<int:category_id>',delete_category),
    path('deleteproduct/<int:product_id>',delete_product),
    path('updatecategory/<int:category_id>',update_category),
    path('updateproduct/<int:product_id>',update_product),

]