import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


def get_upload_user_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "profile", str(instance.id), filename])


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, related_name="Profile", on_delete=models.PROTECT)
    phone = models.CharField(max_length=12)
    image = models.ImageField(
        upload_to="profile/", default="no-profile-picture.jpg", null=True, blank=True)
    description = models.TextField("Descripción", null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.username
