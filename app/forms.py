from django import forms
from app.views import *
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class webpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields='__all__'

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'