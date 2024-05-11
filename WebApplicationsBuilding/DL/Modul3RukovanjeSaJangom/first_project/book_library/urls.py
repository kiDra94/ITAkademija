from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name = 'main_page'),
    path('books/', views.index, name = 'index_page'),
    path('books/<int:int_key>/', views.int_test, name = 'int_test'), #mapirani svi linkovi koji pocinju sa books/(pa ovdje cijeli broj posto je int)
    path('books/<str:book_name>/', views.index, name = 'str_test'), #mapirani svi linkovi koji pocinju sa books/(pa ovdje books_name)
    path('add-book', views.get_book, name = 'book_added'),
    path('book-added', views.redirect_test, name = "redirect")
]