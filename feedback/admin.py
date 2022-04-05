from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Feedback



@admin.register(Feedback)
class FeedbackView(SummernoteModelAdmin):
    """ A dislay to see the feedback text and guest who wrote it """
    list_display = ('text', )