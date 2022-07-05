from django.forms import ModelForm
from django import forms

from .models import Sondage,Comment,Product , Question , Course

###############
from django import forms
from django.contrib.auth.models import User
from . import models

###############

class CreateSondageForm(ModelForm):
    class Meta:
        model = Sondage
        fields = ['question', 'option_one', 'option_two', 'option_three']




class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'price', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name' : 'Enter Product Name:',
            'image': 'Select an Image: ',
            'price': 'Enter a price: ',
            'description': 'Enter a Description: ',
        }
   


##################################################################################################################

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['course_name']

class QuestionForm(forms.ModelForm):
    
    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Survey Name", to_field_name="id")
    class Meta:
        model=models.Question
        fields=['marks','question','option1','option2','option3','option4']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

    

   