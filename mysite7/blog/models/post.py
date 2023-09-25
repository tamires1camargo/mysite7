from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name
