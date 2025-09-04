from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", null=True, blank=True)
    # file = models.FileField(upload_to="project_files/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'title')
    
    def __str__(self):
        return f"{self.title} ({self.technology})"