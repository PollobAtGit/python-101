from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text + " => " + str(self.pub_date)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Computer(models.Model):
    processor_brand = models.TextField(verbose_name="PROCESSOR")
    price = models.DecimalField(verbose_name="PC Price", decimal_places=2, max_digits=10)
