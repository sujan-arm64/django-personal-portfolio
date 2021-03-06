from django.db import models


class NewsletterUsers(models.Model):
    email = models.EmailField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email