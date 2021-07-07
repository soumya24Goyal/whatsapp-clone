from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_email(email,otp):
    subject="OTP: "
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email,]
    send_mail(subject,otp,email_from,recipient_list)
    return "Email send sucessfully" 

