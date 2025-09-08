from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    date_unsubscribed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email
