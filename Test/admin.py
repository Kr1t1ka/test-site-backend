from django.contrib import admin

from .models import Question, Answer, User, Steps, Result

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)
admin.site.register(Steps)
admin.site.register(Result)
