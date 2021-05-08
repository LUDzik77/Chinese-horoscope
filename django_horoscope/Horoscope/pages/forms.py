from django import forms

BIRTH_YEAR_CHOICES = ["1985","1986", "1987","1988", "1989", "1990"]

class GiveYearForm(forms.Form):
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))