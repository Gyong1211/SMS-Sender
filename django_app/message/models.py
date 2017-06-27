from django.db import models


class Message(models.Model):
    sender = models.CharField(max_length=20)
    recipient = models.CharField(max_length=20)
    content = models.CharField(max_length=45)
    send_time = models.DateTimeField(auto_now_add=True)
