from django.forms import ModelForm
from website.models import Newsletter
from blog.models import Comment

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','message','post']