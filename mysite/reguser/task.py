from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(email):
    subject = 'Welcome to our site!'
    message = 'Thank you for registering on our site.'
    from_email = 'kroshakov@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
