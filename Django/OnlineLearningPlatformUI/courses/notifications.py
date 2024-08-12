from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course,Content,Enrollment
from users.models import User
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save,sender=Course)
def course_notification(sender,instance,created, **kwargs):
    print('signal recived,notification sending!!')
    teacher = instance.teacher
    course = instance.name
    subscribers = [student.email for student in User.objects.filter(enrollment__course__teacher=teacher).distinct()]

    send_mail(
            f"New Course {course} Added!",
            f"""Hi Learner,

Good news! Instructor {teacher.name} just added a new course, {course}. Dive into the new Course and continue your learning journey.

Log in now and check it out!

Happy learning,
Online Learning Platform""",
            settings.DEFAULT_FROM_EMAIL,
            subscribers,
            fail_silently=False,
        )

@receiver(post_save,sender=Content)
def content_notification(sender,instance,created, **kwargs):
    print('signal recived,notification sending!!')
    course = instance.course
    enrollment = Enrollment.objects.filter(course = course)
    subscribers = [entry.student.email for entry in enrollment]
    print(course,subscribers)

    send_mail(
            f"Course Update {course.name}!",
            f"""Hi Learner,

Good news! The teacher just added fresh content to your course, {course.name}. Dive into the new content and continue your learning journey.

Log in now and check it out!

Happy learning,
Online Learning Platform""",
            settings.DEFAULT_FROM_EMAIL,
            subscribers,
            fail_silently=False,
        )

@receiver(post_save,sender=Enrollment)
def enroll_notification(sender,instance,created, **kwargs):
    print('signal recived,notification sending!!')
    course = instance.course

    send_mail(
    f"Welcome to {course.name}! You're Successfully Enrolled!",
    f"""Hi Learner,

Congratulations! You have successfully enrolled in the course {course.name}. We're excited to have you on board for this learning journey.

Log in now to start exploring the course content and take your first steps towards mastering new skills.

If you have any questions or need assistance, don't hesitate to reach out.

Happy learning,
Online Learning Platform""",
    settings.DEFAULT_FROM_EMAIL,
    [instance.student.email],
    fail_silently=False,
)
