from django.urls import path

from .views import (
    products_page,
    ProductListView,
    detail_view_product_page,
    SearchListView,
    render_partial_category,
    ProductCategoryListView,
)

app_name = "eshop_products"

urlpatterns = [
    path('products-f', products_page),
    path('products', ProductListView.as_view(), name='products'),
    path('search', SearchListView.as_view()),
    path('products/product/<productId>/<t>', detail_view_product_page, name='product'),
    path('products/<categoryName>', ProductCategoryListView.as_view(), name='products-category'),
    path('partial-catgory', render_partial_category, name='category'),

]
