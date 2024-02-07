from django.urls import path
from .views import *


urlpatterns=[
    path('',index),
    path('productdetails/<int:product_id>',product_details),
    path('productlist/',products),
    path('register/',register_user),
    path('login/',user_login),
    path('logout/',logout_user),
    path('addtocart/<int:product_id>',add_to_cart),
    path('cart/',show_user_cart_items),
    path('removecart/<int:cart_id>',remove_cart),
    path('postorder/<int:product_id>/<int:cart_id>',post_order),
    path('esewa_verify/',esewa_verify),
    path('myorder/',my_order),
    path('esewa-form/',EsewaView.as_view(),name='esewaform'),
    path('esewaverify/<int:order_id>/',esewaVerify)
]