from django.urls import path
from . import views

urlpatterns = [
    path('inputbook/', views.add_book, name='add-book'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('boards/', views.list_books, name='boards'),
]
