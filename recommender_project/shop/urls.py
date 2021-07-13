from django.urls import path
from . import views

urlpatterns = [
    path('greeting', views.greeting),
    path('products', views.product_list),
    path('product/<id>', views.product),
    path('add-product/<name>', views.add_product),
    path('introduction', views.introduction),
    path('product-page/<id>', views.product_page),
    path('report', views.report),
    path('login-page', views.login_page),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('get-data', views.get_data),
    path('redirect', views.redirect_page),
]