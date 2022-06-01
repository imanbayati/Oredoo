from django.forms import ModelForm
from website.models import Newsletter

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'