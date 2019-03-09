from django import forms
from .models import Movie_Post


def GetFileList():
    display = []
    for i in Movie_Post.objects.all():
        display.append((str(i.pk), i.video.name.split('/')[-1]))
    return display


class MyForm(forms.Form):
        List_of_Files = forms.ChoiceField(widget=forms.RadioSelect, choices=GetFileList())

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['List_of_Files'].choices = GetFileList()