from django import forms
from .models import Anime, Studio

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ('name', 'genre', 'description', 'releaseYear', 'studio')
        labels = {'releaseYear': 'Release Year'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['studio'].choices = [(studio.id, studio.name) for studio in Studio.objects.all()]