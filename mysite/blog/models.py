from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tags = TaggableManager()
    content = models.TextField() 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:view", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.title 
