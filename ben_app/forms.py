from django import forms
from ben_app.models import Message

class NewMessage(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message...'}))

    class Meta():
        model = Message
        fields = '__all__'


#    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
#    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message...'})
