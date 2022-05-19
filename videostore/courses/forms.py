from django import forms
from .models import Course, Comment


class CourseAddForm(forms.ModelForm):
        img = forms.ImageField(required=False)

        def __init__(self, *args, **kwards):
            super(CourseAddForm, self).__init__(*args, **kwards)

            self.fields['slug'].label = "Название URL"
            self.fields['title'].label = "Название курса"
            self.fields['description'].label = "Описание курса"
            self.fields['img'].label = "Изображение профиля"

        class Meta:
            model = Course
            fields = ['slug', 'title', 'description', 'img']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'user', 'lesson']

        widgets = {'user': forms.HiddenInput(), 'lesson': forms.HiddenInput()}