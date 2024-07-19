from .models import contact,Comment
from django.forms  import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model=contact 
        fields=["name","y_email","y_subject","y_message"]
       
        
#Comment
class CommentForm(ModelForm): 
    class Meta:
        model=Comment
        fields=['name','email','body']