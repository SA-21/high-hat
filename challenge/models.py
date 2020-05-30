from django.db import models

class Sample(models.Model):
    title = models.CharField(max_length = 200)
    photo = models.ImageField(blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.summary[:30]
