from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    def published_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pud_date <= now

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
