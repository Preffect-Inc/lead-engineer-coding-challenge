from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    signup_date = models.DateField()
    age = models.IntegerField()
    height_cm = models.IntegerField()
    weight_kg = models.IntegerField()
    activity_level = models.CharField(max_length=20)
    health_goals = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.user_id})"
