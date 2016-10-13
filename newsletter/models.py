from django.db import models


# from django.utils import timezone


class SignUp(models.Model):
    email = models.EmailField(default='')
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
