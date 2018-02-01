from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, DateTimeInput, Textarea
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question_text': Textarea(attrs={'cols': 80, 'rows': 20}),
            'pub_date': DateTimeInput(),   
        }
        labels = {
            'question_text': _('Question'),
        }    
