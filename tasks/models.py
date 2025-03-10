from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ('Overdue', 'Overdue'),
        ('Due Today', 'Due Today'),
        ('Upcoming', 'Upcoming'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        today = date.today()
        
        if self.due_date < today:
            self.status = 'Overdue'
        elif self.due_date == today:
            self.status = 'Due Today'
        else:
            self.status = 'Upcoming'
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
