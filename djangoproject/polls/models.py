from django.db import models

# Create your models here.
class Questions(models.model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.model):
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length= 100)
    votes =models.IntegerField(default = 0)
    