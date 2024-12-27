from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, null=True,max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.ForeignKey('priority', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class priority(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

