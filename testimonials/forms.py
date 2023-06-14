from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'testimonial', 'rating']
        labels = {
            'name': 'Name',
            'testimonial': 'Testimonial',
            'rating': 'Rating (out of 5)',
        }