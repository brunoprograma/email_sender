import requests

from celery.utils.log import get_task_logger
from django.conf import settings

from email_sender.celery import app

logger = get_task_logger(__name__)


@app.task(name="send_simple_message")
def send_simple_message(email):
    logger.info('Creating new task...')

    subject = 'Subject example'
    from_email = settings.EMAIL_HOST_USER
    message = 'Message example'
    to = email

    requests.post(
        "https://api.mailgun.net/v3/sandboxd118479765714f6ba2889892a22d5bb0.mailgun.org/messages",
        auth=("api", "c90a190ebea0017017275e4937b22518-30b9cd6d-730d8e7a"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxd118479765714f6ba2889892a22d5bb0.mailgun.org>",
              "to": "Bruno Ribeiro <brunoribeiroinf@gmail.com>",
              "subject": "Hello Bruno Ribeiro",
              "text": "Congratulations Bruno Ribeiro, you just sent an email with Mailgun!  You are truly awesome!"})

    logger.info('Finished new task schedule...')
