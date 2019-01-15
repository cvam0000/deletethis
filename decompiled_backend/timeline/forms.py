from django import forms

class ContactForm(forms.Form):
    author = forms.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = forms.CharField(max_length=100)
    update = forms.CharField(widget=forms.Textarea)
    created_date = forms.DateTimeField(default=timezone.now)
    published_date = forms.DateTimeField(blank=True, null=True)
    cc_myself = forms.BooleanField(required=False)
