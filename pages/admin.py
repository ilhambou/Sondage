from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Category)

# class AnswerAdmin(admin.StackedInline):
#     model = Answer

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerAdmin]


# admin.site.register(Question,QuestionAdmin)
# admin.site.register(Answer)

admin.site.register(Sondageglob)
admin.site.register(Sondage)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)





