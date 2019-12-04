from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default=None)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now_add=True)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
