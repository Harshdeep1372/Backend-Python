
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('shop-grid/',views.shop_grid,name="shop-grid"),
    path('shop-details/',views.shop_details,name="shop-details"),
    path('shoping-cart/',views.shoping_cart,name="shoping-cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('contact/',views.contact,name="contact"),  
    path('signup/',views.signup,name="signup"),  
    path('login/',views.login,name="login"),  
    path('logout/',views.logout,name="logout"),
    path('change-password/',views.change_password,name="change-password"),
    path('profile/',views.profile,name="profile"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('verify-otp/',views.verify_otp,name="verify-otp"),
    path('new-password/',views.new_password,name="new-password"),


]
