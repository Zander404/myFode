from django import urls
from django.urls import path
from loja import views


urlpatterns = [


    #Home
    path('', views.index, name='index'),
    path('', views.index, name='paginaInicial'),


    # #Products
    path('category-list/', views.category_list, name='category-list'),
    path('product-list/', views.product_list, name='product-list'),
    path('marca-list/', views.marca_list, name='marca-list'),
    path('size-list/', views.size_list, name='size-list'),

    # path('category/<int:category_id>/', views.category, name='category'),
    # path('product/<int:product_id>/', views.product, name='product'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('order/', views.order, name='order'),
    # path('order_complete/', views.order_complete, name='order_complete'),
    
    # #Login
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('register/', views.register, name='register'),
    
    #Cart
    path('cart/', views.cart, name='cart'),

    path('search/', views.search, name='search'),
    
    #
    # # Profile
    #
    # path('profile/', views.profile, name='profile'),
    # path('profile_edit/', views.profile_edit, name='profile_edit'),
    # path('profile_password/', views.profile_password, name='profile_password'),
    # path('profile_address/', views.profile_address, name='profile_address'),
    # path('profile_address_edit/<int:address_id>/', views.profile_address_edit, name='profile_address_edit'),
    # path('profile_address_delete/<int:address_id>/', views.profile_address_delete, name='profile_address_delete'),
    # path('profile_address_add/', views.profile_address_add, name='profile_address_add'),

    ]