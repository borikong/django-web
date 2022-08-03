from django import forms


class PostForm(forms.Form):
    postname=forms.CharField(error_messages={'requierd':'제목을 입력해 주세요'},max_length=128,label="Title")
    contents=forms.CharField(error_messages={'requierd':'내용을 입력해 주세요'},widget=forms.Textarea,label="Content")
    