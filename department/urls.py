from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('staff/', views.StaffListView.as_view(), name='staff_list'),
    path('timetables/', views.TimetableView.as_view(), name='timetable_list'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
   
]