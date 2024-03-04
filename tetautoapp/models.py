from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)  # Optional field
    phone_number = models.CharField(max_length=20, blank=True)  # Optional field
    email = models.EmailField()
    message = models.TextField()
    topic_choices = (
        ('enquiry', 'Enquiry'),
        ('sales', 'Sales'),
        ('support', 'Support'),
    )
    topic = models.CharField(max_length=20, choices=topic_choices)

    def __str__(self):
        return self.name


# Create your models here.
