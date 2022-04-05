from django import forms
from django.forms import ModelForm
from .models import Feedback


class FeedbackForm(ModelForm):
    """ A form to handle the feedback posting """
    class Meta:
        model = Feedback
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'How was your stay...?'})