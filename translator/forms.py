
from django import forms

class TranslationForm(forms.Form):
    text_to_translate = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'your-css-classes-here', 'rows': 4, 'cols': 40})
    )
    
    target_language = forms.ChoiceField(label='Target Language', choices=[('en', 'English'), ('ta', 'Tamil'), ('hi', 'Hindi'), ('fr', 'French')], 
                                        widget=forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500'}))
    
    source_language = forms.ChoiceField(label='Source Language', choices=[('en', 'English'), ('ta', 'Tamil'), ('hi', 'Hindi'), ('fr', 'French')], 
                                        widget=forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500'}))
