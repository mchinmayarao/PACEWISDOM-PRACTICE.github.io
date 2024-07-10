from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='img1.png' , blank=True)

    def __str__(self):
        return f"title: {self.title}\nbody: {self.body}\nslug: {self.slug}\ndate: {self.date}\n"
    