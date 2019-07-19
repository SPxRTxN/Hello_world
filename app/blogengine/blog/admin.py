from django.contrib import admin
# from .models import House
# #
# #
# # @admin.register(House)
# # # Register your models here.
# # class AdminHouse(admin.ModelAdmin):
# #     pass

from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
