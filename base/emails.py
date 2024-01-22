from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = 'Your account need to be verify'
    email_form = settings.EMAIL_HOST_USER
    message =f'Hi,Click On the link to activate Your account http://127.0.0.1:8000/activate/{email_token}'
    send_mail(subject,message,email_form,[email])