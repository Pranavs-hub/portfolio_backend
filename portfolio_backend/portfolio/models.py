from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name