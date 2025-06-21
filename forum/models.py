from django.db import models
from django.conf import settings

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='answer_upvotes', blank=True)
    downvotes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='answer_downvotes', blank=True)

    def score(self):
        return self.upvotes.count() - self.downvotes.count()


    def __str__(self):
        return f"Answer by {self.author.username} on {self.question.title}"
