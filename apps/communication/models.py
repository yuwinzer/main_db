from django.db import models

from apps.customers.models import Customer, Source
from apps.users.models import User


class Message(models.Model):
    datetime = models.DateTimeField()
    text = models.TextField(max_length=10000)
    place = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    link = models.CharField(max_length=1048)
    is_sent_to_customer = models.BooleanField()

    class Meta:
        db_table = "messages"


class Question(models.Model):
    text = models.TextField(max_length=500)

    class Meta:
        db_table = "questions"


class AnswerTemplate(models.Model):
    question = models.ManyToManyField(Question)
    text = models.TextField(max_length=10000)

    class Meta:
        db_table = "answer_templates"


