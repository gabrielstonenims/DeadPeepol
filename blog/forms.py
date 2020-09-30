from django import forms
from .models import TrackByEmail,VerifyEmail



class GetAlbumByEmailForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your valid email address.'}))

    class Meta:
        model = TrackByEmail
        fields = ['email']

class VerifyEmailForm(forms.ModelForm):

    class Meta:
        model = VerifyEmail
        fields = ['youremail']


class ConfirmAndDownload(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email provided earlier','id':'verifiedemail'}))
    code = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder':'Enter code given to you.'}))
    