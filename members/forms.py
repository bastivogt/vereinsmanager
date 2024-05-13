from django import forms


class FrontendMembersFilterForm(forms.Form):
    genders = forms.Select()