"""
URL configuration for Moda_Peluda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products import views as productViews
from accounts import views as accountViews
from cart import views as cartViews
from orders import views as orderViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',productViews.home_view,name=''),
    path('detail/<int:pk>', productViews.product_detail_view,name='detail'),
    path('create/', productViews.crate_product_view, name='create-product'),
    path('update-product/<int:pk>', productViews.update_product_view,name='update-product'),
    path('delete-product/<int:pk>', productViews.delete_product_view,name='delete-product'),
    
    path('create-collar/', productViews.create_collar_view, name='create-collar'),
    
    path('signup-account/', accountViews.signup_account_view,name='signup-account'),
    path('logout-account/', accountViews.logout_account_view,name='logout-account'),
    path('login-account/', accountViews.login_account_view,name='login-account'),
    
    path('add-to-cart/<int:pk>', cartViews.add_to_cart_view,name='add-to-cart'),
    path('cart', cartViews.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', cartViews.remove_from_cart_view,name='remove-from-cart'),

    path('checkout', orderViews.create_order,name='checkout'),
    path('checkout/confirmation/<int:order_id>/', orderViews.order_confirmation, name='order_confirmation'),
    path('checkout/statistics', orderViews.view_stadistics,name='stadistics'),

    path('search', productViews.search_view, name='search'),
    path('payment/', orderViews.payment_view, name='payment'),
    
    
    # API #
    path('api/collares-creados/', productViews.get_personalized_collar_view, name='api_collares_stock'),
]
