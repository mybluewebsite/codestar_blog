from django.db import models
from django.contrib.auth.models import User # Import models to connect
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(default="")
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_on"]
    
        def __str__(self):
            return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    challenge = models.FloatField(default=3.0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(default="")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

        def __str__(self):
            return f"Comment {self.body} by {self.author} on {self.post.title}"