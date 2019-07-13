from django import forms

from .models import Movie


class MovieCreationForm(forms.ModelForm):
    STARS_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    stars = forms.ChoiceField(choices=STARS_CHOICES)

    class Meta:
        model = Movie
        fields = (
            'title',
            'director',
            'writer',
            'year',
            'summary',
            'stars',
            'category',
        )

    def clean(self):
        if (int(self.cleaned_data['stars']) > 5 or
            int(self.cleaned_data['stars']) < 0):
            self.add_error('stars', 'invalid value for stars')