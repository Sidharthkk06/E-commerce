from django.urls import path
from Eshop import views

urlpatterns=[
    path('',views.Home.as_view(), name = "home"),
    path('category/<int:cd>',views.CategoryDetail.as_view(),name = "category"),
    path('product/<int:pid>',views.ProductDetail.as_view(),name = "prod"),
    path('cart/<int:pid>',views.AddToCart.as_view(), name = "cart"),
    path('cart_delete/<int:pid>',views.CartDelete.as_view(), name = "cart_del"),
    path('cartdetail/',views.CartDetail.as_view(), name="cart_detail"),
    path('register/',views.RegisterView.as_view(), name="register"),
    path('signin/',views.SignInView.as_view(), name = "login"),
    path('logout/',views.SignOutView.as_view(), name = "logout"),
]