from django.db import models
from .tasks import send_simple_message


class Recipient(models.Model):
    """
    Recipient who's gonna receive the messages
    """
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'


STATUS_COICES = [
    ('s', 'Sent'),
    ('f', 'Failed'),
    ('p', 'Pending')
]


class EmailMessage(models.Model):
    """
    Messages that we got to send
    """
    subject = models.CharField(max_length=100)
    message = models.TextField()
    recipients = models.ManyToManyField(Recipient)
    status = models.CharField(max_length=1, choices=STATUS_COICES,
                              editable=False, default='p')  # can't be changed in forms
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject}'

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
        if self.status == 'p':  # if message is pending we schedule the sending
            send_simple_message.delay(self)

    class Meta:
        verbose_name = 'E-mail Message'
        verbose_name_plural = 'E-mail Messages'
