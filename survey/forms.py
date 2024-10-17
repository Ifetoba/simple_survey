from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=50)   # Add username field
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))


class SurveyForm(forms.Form):
    question_1 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 1'}), required=True)
    question_2 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 2'}), required=True)
    question_3 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 3'}), required=True)
    question_4 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 4'}), required=True)
    question_5 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 5'}), required=True)
    question_6 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 6'}), required=True)
    question_7 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 7'}), required=True)
    question_8 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 8'}), required=True)
    question_9 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 9'}), required=True)
    question_10 = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Answer question 10'}), required=True)
