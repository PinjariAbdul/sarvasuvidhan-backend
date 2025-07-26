from django.db import models

class FormData(models.Model):
    form_number = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.form_number
