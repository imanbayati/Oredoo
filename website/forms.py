from django.forms import ModelForm
from website.models import Newsletter,Contact

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'    