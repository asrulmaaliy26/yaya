from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def index(request):
    content = [
        {'icon': 'fas fa-chalkboard-teacher', 'number': 271, 'description': 'Pendidik & Tenaga Kependidikan'},
        {'icon': 'fas fa-user-graduate', 'number': 13132, 'description': 'Peserta Didik'},
        {'icon': 'fas fa-graduation-cap', 'number': 12580, 'description': 'Alumni'},
        {'icon': 'fas fa-clipboard-list', 'number': 15983, 'description': 'Pendaftar Calon Peserta Didik'},
    ]
    
    events = Article.objects.all()  # Ambil semua event dari model
    print(events)
    
    return render(request, 'index.html', {'content': content, 'events': events})