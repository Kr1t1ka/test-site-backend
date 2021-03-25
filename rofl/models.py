from django.db import models


# Create your models here.

class Answer(models.Model):
    text = models.CharField(max_length=1000, verbose_name='Ответ', default='Я, Ничего, Тут')

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.CharField(max_length=2000, verbose_name='Вопрос', default='Кто? Что? Где?')
    score = models.FloatField(verbose_name='Веса для вопроса', default=0.5)
    answer = models.ManyToManyField(Answer, verbose_name='вопрос к ответу')

    def __str__(self):
        return self.text


class User(models.Model):
    jwt = models.TextField(verbose_name='токен пользователя')

    def __str__(self):
        return self.jwt


class Steps(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='вопрос', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, verbose_name='ответ', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.answer}'
