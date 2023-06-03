from django import forms

from .models import (Post, Group, Answer)


class PostForm(forms.ModelForm):

    text = forms.CharField(max_length=200, required=False,
                           widget=forms.Textarea(
                                                     attrs = {
                                                               'placeholder':
                                                               "Write something"
                                                             } 
                                                  ))
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)

    class Meta:

        model = Post
        fields = [
            'text',
            'image',
            'video'
        ] 


class GroupForm(forms.ModelForm):
    
    banner = forms.ImageField(required=False)
    image = forms.ImageField(required=False)
    name = forms.CharField(max_length=50,
                            widget=forms.TextInput(
                                                     attrs = {
                                                               'placeholder':
                                                               "Your group name"
                                                             } 
                                                  )
                            )
    field = forms.CharField(max_length=50, 
                            widget=forms.TextInput(
                                                     attrs = {
                                                               'placeholder':
                                                               "Your group field"
                                                             } 
                                                  )
                           )
    des = forms.CharField(max_length=150, 
                          widget=forms.Textarea(
                                                  attrs = {
                                                            'placeholder':
                                                            "Your Description"
                                                          }
                                               )
    )

    class Meta:

        model = Group
        fields = [
            'banner',
            'image',
            'name',
            'field',
            'des'
        ]


class AnswerForm(forms.ModelForm):

    text = forms.CharField(max_length=300,
                           widget=forms.Textarea(
                                                   attrs={
                                                            'placeholder':"Your Awnser"
                                                         }
                                                )
                           )
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)

    class Meta:

        model = Answer
        fields = [
            'text',
            'image',
            'video'
        ]                