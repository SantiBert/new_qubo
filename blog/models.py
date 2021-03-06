import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from colorfield.fields import ColorField
# Create your models here.


def get_upload_blog_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "blog", str(instance.blog.id), filename])


class BlogCategory(models.Model):
    # Modelo para crear categoria
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    slug = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='category/', default="image_placeholder.jpg", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    color = ColorField(default='#28a745')

    def __str__(self):
        return self.name


class BlogEntry(models.Model):
    # Modelo para crear post
    user = models.ForeignKey(User, related_name="users",
                             on_delete=models.PROTECT)
    name = models.CharField(max_length=128, null=True, blank=True)
    category = models.ManyToManyField(BlogCategory, related_name="categories")
    created_date = models.DateTimeField(default=timezone.now)
    description = RichTextUploadingField(null=True, blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    image_ref = models.ImageField(
        upload_to='blog/', default="image_placeholder.jpg", null=True, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return "blog: {} // De: ".format(self.name, self.user.username)
