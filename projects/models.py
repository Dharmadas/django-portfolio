from django.db import models

class Project(models.Model):
    heading = models.CharField(null=True, max_length=40)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.heading
