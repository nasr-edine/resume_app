from django.db import models
from django.urls import reverse


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):  # new
    #     return reverse('main:index')
