from django.db import models


class Recipient(models.Model):
    """
    Recipient who's gonna receive the messages
    """
    email = models.EmailField(unique=True)


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
                              editable=False, default='pending')  # can't be changed in forms
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'E-mail Message'
        verbose_name_plural = 'E-mail Messages'
