from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER

# to_emails, tupla o array
def send_notification(users,msg,subject='Notifica da Progetto tech web.'):
    send_mail(
        subject,
        msg,
        EMAIL_HOST_USER,
        [u.email for u in users],
        fail_silently=False,
    )
