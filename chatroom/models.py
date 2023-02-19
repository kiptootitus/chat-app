from django.db import models
from django.contrib.auth.models import User

class Chatroom(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField()
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} in {self.chatroom.name}: {self.text}'
