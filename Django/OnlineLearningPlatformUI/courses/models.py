from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField( max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    teacher = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course", kwargs={"pk": self.pk})

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey("Course",on_delete=models.CASCADE)

    
class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
    ]

    enrolled_at = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey("users.User", on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def update_status(self):

        if self.status == 'active' and timezone.now() >= self.enrolled_at + timezone.timedelta(minutes=3):
            self.status = 'expired'
            super().save(update_fields=['status'])  

    def save(self, *args, **kwargs):
        super(Enrollment, self).save(*args, **kwargs)