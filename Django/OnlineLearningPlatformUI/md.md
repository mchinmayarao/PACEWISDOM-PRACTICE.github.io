To achieve this, you'll need to update the `Enrollment` model to include a `status` field, add a method to update the status after 10 minutes, and modify the `is_enrolled_or_teacher` decorator to check this status. Here's how you can do it:

### 1. Update the `Enrollment` Model
Add a `status` field to track whether the course is active or expired.

```python
from django.utils import timezone
from django.db import models

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
        if timezone.now() >= self.enrolled_at + timezone.timedelta(minutes=10):
            self.status = 'expired'
            self.save()

    def save(self, *args, **kwargs):
        self.update_status()
        super(Enrollment, self).save(*args, **kwargs)
```

### 2. Modify the `is_enrolled_or_teacher` Decorator
Update the decorator to check the `status` of the enrollment before granting access.

```python
from functools import wraps
from django.http import HttpResponse
from .models import Enrollment, Course

def is_enrolled_or_teacher(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        course = Course.objects.get(name=kwargs['name'])
        if request.user.is_authenticated:
            if request.user == course.teacher:
                return view_func(request, *args, **kwargs)
            try:
                enrollment = Enrollment.objects.get(student=request.user, course=course)
                enrollment.update_status()  # Ensure status is up-to-date
                if enrollment.status == 'active':
                    return view_func(request, *args, **kwargs)
            except Enrollment.DoesNotExist:
                pass
        return HttpResponse("<h1>Purchase the course </h1>")
    return _wrapped_view
```

### Explanation:

1. **`Enrollment` Model Changes:**
    - Added a `status` field with choices for `active` and `expired`.
    - `update_status` method updates the status to `expired` if 10 minutes have passed since `enrolled_at`.
    - The `save` method is overridden to automatically check and update the status every time the enrollment is saved.

2. **Decorator Changes:**
    - The decorator now checks if the user is the course teacher or has an active enrollment. If the enrollment is expired, access is denied.