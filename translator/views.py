# views.py
from django.shortcuts import render
from .forms import TranslationForm
import requests

def translate_text(text, target_language, source_language):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "target": target_language,
        "source": source_language
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "a37bd030e7msh91a64a815db01f8p1e46b3jsn13c4aec2e158",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    
    if response.ok:
        return response.json()
    else:
        return {'error': {'message': f"Translation API Error: {response.status_code} - {response.reason}"}}

def index(request):
    form = TranslationForm()
    translation_result = None

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text_to_translate = form.cleaned_data['text_to_translate']
            target_language = form.cleaned_data['target_language']
            source_language = form.cleaned_data['source_language']

            translation_result = translate_text(text_to_translate, target_language, source_language)

            if 'error' in translation_result:        
                form.add_error(None, translation_result['error']['message'])

    context = {
        'form': form,
        'translation_result': translation_result,
    }


    return render(request, 'home.html', context)
