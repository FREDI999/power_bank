from django.urls import path
from products.views import WishlistPageView, add_to_wishlist, accounts

app_name = "products"

urlpatterns = [
    path('wishlist/', WishlistPageView.as_view(), name="wishlist"),
    path('accaunts/', accounts, name="accaunts"),
    path('<int:product_pk>/add_to_wishlist/', add_to_wishlist, name="add_to_wishlist")
]