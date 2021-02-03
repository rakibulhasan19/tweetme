from django import forms
from .models import Tweets

MAX_TWEET_LENGTH = 240
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['contant']
    def clean_content(self):
        contant = self.cleaned_data.get("contant")
        if len(contant) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("this tweet is too long..")
        return contant