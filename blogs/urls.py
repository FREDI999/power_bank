from django.urls import path
from blogs.views import posts, details, commentary, massage

app_name = "blogs"

urlpatterns = [
    path('posts/', posts, name="posts"),
    path('<int:pk>/details/', details, name="details"),
    path('commentry/', commentary, name="coment"),
    path('massage/', massage, name="massage"),
]