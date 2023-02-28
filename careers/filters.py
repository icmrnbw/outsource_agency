from django import forms
from django_filters import FilterSet, ModelChoiceFilter

from .models import Vacancy, VacancyCategory, Location


class VacancyFilter(FilterSet):
    """
    Filter to search posts by name and category.
    """
    location = ModelChoiceFilter(queryset=Location.objects.all(), widget=forms.Select(attrs={'class': 'dropdown location-select', 'id': 'locations-dropdown'}))
    category = ModelChoiceFilter(queryset=VacancyCategory.objects.all(), widget=forms.Select(attrs={'class': 'dropdown category-select', 'id': 'categories-dropdown'}))

    class Meta:
        model = Vacancy
        fields = [
            'location',
            'category',
        ]