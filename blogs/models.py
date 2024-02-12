from django.db import models

# Create your models here.

class PostsModel(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField()
    title = models.CharField(max_length=90)
    desctiption = models.CharField(max_length=250)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.created_at}"
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class CommentariyModel(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    commentary = models.TextField()


class MassageModel(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    commentary = models.TextField()
    