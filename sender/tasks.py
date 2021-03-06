import requests
from celery.utils.log import get_task_logger
from django.conf import settings
from email_sender.celery import app

logger = get_task_logger(__name__)


@app.task(name="send_simple_message")
def send_simple_message(emailmessage_id):
    """
    Receives a instance from sender.models.EmailMessage and sends the message
    """
    logger.info('Creating new task...')
    from .models import EmailMessage

    try:
        emailmessage = EmailMessage.objects.get(id=emailmessage_id)
    except EmailMessage.DoesNotExist:  # probably deleted
        logger.info(f'Message {emailmessage_id} not found')
        return

    subject = emailmessage.subject
    from_email = settings.EMAIL_HOST_USER
    message = emailmessage.message
    to = ', '.join(emailmessage.recipients.values_list('email', flat=True))
    url = settings.MAIL_URL
    secret = settings.MAIL_SECRET

    logger.info(f'Sending message to {to} through API {url}')

    try:
        response = requests.post(
            url,
            auth=("api", secret),
            data={"from": from_email,
                  "to": to,
                  "subject": subject,
                  "text": message})
    except Exception as e:
        logger.exception(f'Exception at sending e-mail: {emailmessage} ({e})')
        emailmessage.status = 'f'
        emailmessage.save()
    else:
        if response.status_code == 200:
            emailmessage.status = 's'
            emailmessage.save()
        else:
            logger.error(f'Error at sending e-mail: {emailmessage} ({response.status_code}: {response.content})')
            emailmessage.status = 'f'
            emailmessage.save()

    logger.info('Finished new task schedule...')
