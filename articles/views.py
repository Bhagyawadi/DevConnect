from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

from django.core.paginator import Paginator

def article_list(request):
    query = request.GET.get('q')
    article_list = Article.objects.all()
    if query:
        article_list = article_list.filter(title__icontains=query)
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'articles/article_list.html', {'articles': articles, 'query': query})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:detail', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

@login_required
def article_edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user != article.author:
        return redirect('articles:detail', slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', slug=slug)
    return render(request, 'articles/article_form.html', {'form': form})

@login_required
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user == article.author:
        article.delete()
    return redirect('articles:list')
