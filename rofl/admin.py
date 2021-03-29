from django.contrib import admin

from .models import Question, Answer, User, Steps, Faculty

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)
admin.site.register(Steps)
admin.site.register(Faculty)
