from django.db import models

# Create your models here.
"""
schema  :QuestionsDb
fields  :question,option_a,option_b,option_c,option_d,correct_answer
"""
class QuestionsDb(models.Model):
    question=models.CharField(max_length=100)
    option_a=models.CharField(max_length=100)
    option_b=models.CharField(max_length=100)
    option_c=models.CharField(max_length=100)
    option_d=models.CharField(max_length=100)
    ANSWER_CHOICE=[("A","a"),("B","b"),("C","c"),("D","d")]
    correct_answer=models.CharField(max_length=100,choices=ANSWER_CHOICE,default="A")

