from django.urls import path
from .views import index, ashyolar, about, contact, detail, gallery, \
    savat, afterContact, ProductsDeleteView, ProductsUpdateView, ProductCreateView, sotuv, SearchResults

urlpatterns = [
    path('', index, name='index'),
    path('ashyolar/', ashyolar, name='ashyolar'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('detail/<slug:products>/', detail, name='detail'),
    path('gallery/', gallery, name='gallery'),
    path('sotuv/', sotuv, name='sotuv'),
    path('products/edit/<slug>/', ProductsUpdateView.as_view(), name='product_update'),
    path('products/delete/<slug>/', ProductsDeleteView.as_view(), name='product_delete'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('savat/', savat, name='savat'),
    path('afterContact/', afterContact, name='afterContact'),
    path('search_results/', SearchResults.as_view(), name='search_results'),
]