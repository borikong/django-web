from django import forms


class PostForm(forms.Form):
    postname=forms.CharField(error_messages={'requierd':'제목을 입력해 주세요'},max_length=128,label="Title")
    name = forms.CharField(error_messages={'requierd': '이름을 입력해 주세요'}, max_length=128, label="Name")
    passwd = forms.CharField(error_messages={'requierd': '비밀번호를 입력해 주세요'}, max_length=128, label="Passwd")
    contents=forms.CharField(error_messages={'requierd':'내용을 입력해 주세요'},widget=forms.Textarea,label="Content")

class DeleteForm(forms.Form):
    passwd=forms.CharField(error_messages={'requierd':'비밀번호를 입력해 주세요'},max_length=128,label="Passwd")