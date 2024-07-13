from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', views.article_list, name='article_list'),
    # path('article/<int:pk>/', views.article_detail, name='article_detail'),
    
    path('', views.index, name=''),
    
    # path('', TemplateView.as_view(template_name='index.html'), name=''),
    path('akreditasi', TemplateView.as_view(template_name='akreditasi.html'), name='akreditasi'),
    path('berita', TemplateView.as_view(template_name='berita.html'), name='berita'),
    path('ekskul', TemplateView.as_view(template_name='ekskul.html'), name='ekskul'),
    path('faqs', TemplateView.as_view(template_name='faqs.html'), name='faqs'),
    path('helpdesk', TemplateView.as_view(template_name='helpdesk.html'), name='helpdesk'),
    path('jurusan', TemplateView.as_view(template_name='jurusan.html'), name='jurusan'),
    path('ma', TemplateView.as_view(template_name='ma.html'), name='ma'),
    path('smp', TemplateView.as_view(template_name='smp.html'), name='smp'),
    path('mahad', TemplateView.as_view(template_name='mahad.html'), name='mahad'),
    path('prestasi', TemplateView.as_view(template_name='prestasi.html'), name='prestasi'),
    path('profil', TemplateView.as_view(template_name='profil.html'), name='profil'),
    path('struktur_organisasi', TemplateView.as_view(template_name='struktur_organisasi.html'), name='struktur_organisasi'),
    path('tpq', TemplateView.as_view(template_name='tpq.html'), name='tpq'),
    path('kampus', TemplateView.as_view(template_name='kampus.html'), name='kampus'),
]