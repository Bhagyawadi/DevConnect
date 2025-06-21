from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('ask/', views.question_create, name='question_create'),
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('answer/<int:pk>/upvote/', views.upvote_answer, name='upvote'),
    path('answer/<int:pk>/downvote/', views.downvote_answer, name='downvote'),

]
