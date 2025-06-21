from django.shortcuts import render , redirect
from django.contrib.auth import login , logout
from .forms import CustomUserCreationForm , ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from articles.models import Article
from forum.models import Question

# Create your views here.

# core/views.py
from django.shortcuts import render

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Update to your home view later
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})

@login_required
def dashboard_view(request):
    user_articles = Article.objects.filter(author=request.user)
    user_questions = Question.objects.filter(author=request.user)
    profile = request.user.profile
    return render(request, 'accounts/dashboard.html', {
        'articles': user_articles,
        'questions': user_questions,
        'profile': profile
    })
    
def logout_view(request):
    logout(request)
    return redirect('accounts:login')