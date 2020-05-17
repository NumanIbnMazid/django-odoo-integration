from django.contrib import admin
from django.urls import path
from .views import HomeView, add_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('add-book/', add_book, name="add_book"),
]
