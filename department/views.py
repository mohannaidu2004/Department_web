from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.views.generic import DetailView
from .models import News

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

def home(request):
    news = News.objects.filter(is_published=True).order_by('-created_at')[:3]
    staff = Staff.objects.all().order_by('order')[:6]
    timetables = Timetable.objects.filter(is_active=True).order_by('-upload_date')[:3]
    gallery_images = GalleryImage.objects.all().order_by('-upload_date')[:8]
    
    context = {
        'news': news,
        'staff': staff,
        'timetables': timetables,
        'gallery_images': gallery_images,
    }
    return render(request, 'home.html', context)

class NewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news_list'
    paginate_by = 10
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-created_at')

class StaffListView(ListView):
    model = Staff
    template_name = 'staff.html'
    context_object_name = 'staff_list'
    
    def get_queryset(self):
        return Staff.objects.all().order_by('order')

class TimetableView(ListView):
    model = Timetable
    template_name = 'timetable.html'
    context_object_name = 'timetables'
    
    def get_queryset(self):
        return Timetable.objects.filter(is_active=True).order_by('-upload_date')

class GalleryView(ListView):
    model = GalleryImage
    template_name = 'gallery.html'
    context_object_name = 'gallery_images'
    paginate_by = 12
    
    def get_queryset(self):
        return GalleryImage.objects.all().order_by('-event_date', '-upload_date')

def contact(request):
    if request.method == 'POST':
        # Process contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactSubmission.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        return render(request, 'contact.html', {'success': True})
    
    return render(request, 'contact.html')