from django.urls import path
from .forms import Login
from django.contrib.auth import views as auth_views ## Here we used views as auth_views because there is already an import named view. 
from . import views                                 ## Hence there will be 2 views. So we changed name of one view as auth_views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=Login),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('become-vendor/', views.vendor_signup, name = 'become_vendor'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('address/',views.AddressCreateView.as_view(), name='address'),
    path('address/update/<pk>', views.AddressUpdateView.as_view(), name='address-edit'),
    path('address/delete/<pk>', views.AddressDeleteView.as_view(), name='address-delete'),
    path('change-password/',views.ChangePassword.as_view(),name='change_password'),
    path('my-orders/',views.my_order,name='my-order'),
    path('my-reviews/',views.my_reviews,name='my-reviews'),
    path('vendor-dash/', views.vendor_dash, name='vendor-dash'),
    path('active-items/', views.active_items, name='active_items'),
    path('edit-seller-profile/', views.edit_seller_profile, name='edit_seller_profile'),
    path('orders/', views.seller_order, name='orders'),
    path('reviews/', views.seller_review, name='reviews'),

] 