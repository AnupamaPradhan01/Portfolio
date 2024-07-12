from .models import contact
from django.forms  import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model=contact 
        fields=["name","y_email","y_subject","y_message"]
       
        