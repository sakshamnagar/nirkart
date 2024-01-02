from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name = "home"),
    path('products/', views.MainCategoryListView, name = "products"),
    path('create/', views.ItemCreateView.as_view(), name = "create_item"),
    path('edit-item/<slug:slug>/', views.ItemUpdateView.as_view(), name='edit_item'),
    path('ajax/sub_category_drop_down/', views.sub_category, name='sub_category'),
    path('search/', views.search, name= 'search'),
    path('products/<slug:slug>/',views.product_detail,name='product_detail'),
    path('delete/<slug:slug>', views.ItemDeleteView.as_view(), name='delete'),
    path('category/<slug:slug>/', views.category_page, name = 'category_page'),
    path('sub-category/<slug:slug>/', views.subcategory_page, name = 'subcategory_page'),
    path('store/<str:vendor>/',views.store,name='store'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)