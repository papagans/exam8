
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webapp.views import IndexView, ProductView, ProductUpdateView, ProductCreateView, ProductDeleteView, \
    OtzivCreateView, OtzivUpdateView, OtzivDeleteView

app_name ='webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('otziv/<int:pk>/create/', OtzivCreateView.as_view(), name='otziv_create'),
    path('otziv/<int:pk>/update/', OtzivUpdateView.as_view(), name='otziv_update'),
    path('otziv/<int:pk>/delete/', OtzivDeleteView.as_view(), name='otziv_delete'),
]