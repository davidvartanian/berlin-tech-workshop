from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=10, null=False, unique=True)
    url = models.CharField(max_length=1024, null=False)

    # owner = models.ForeignKey(User, related_name="links", on_delete=models.CASCADE, null=True)