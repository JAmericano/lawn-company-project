from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ("Basic Lawn Mowing - $65", "Basic Lawn Mowing - $65"),
        ("Fertilization - $40", "Fertilization - $40"),
        ("Full Service Package - $120", "Full Service Package - $120"),
        ("Bush Trimming - $35+", "Bush Trimming - $35+"),
        ("Leaf Cleanup - $45+", "Leaf Cleanup - $45+"),
        ("Sprinkler Check - $50+", "Sprinkler Check - $50+"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return f"{self.name} - {self.service} on {self.date} at {self.time}"