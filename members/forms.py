from django import forms


from . import models

class MemberForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["firstname"].widget.attrs["class"] = "form-control"
        # self.fields["lastname"].widget.attrs["class"] = "form-control"

    class Meta:
        model = models.Member
        fields = "__all__"
        labels = {
            "firstname": "Vorname",
            "lastname": "Nachname",
            "birthday": "Geburtstag",
            "gender": "Geschlecht",
            "adress": "Adresse",
            "email": "E-Mail",
            "phone": "Telefon",
            "entry_date": "Eintrittsdatum",
            "account_details": "Bankverbindung",
            "positions": "Positionen",
            "modules": "Module",
            "chronic_diseases": "Chronische Krankheiten",
            "permanent_medication": "Dauerhafte Medikamente",
            "publish_fotos": "Fotos veröffentlichen",
            "is_active": "Aktiv",
            "legal_representative": "Gesetzlicher Vormund", 
            "rate": "Tarif",
            "licenses": "Lizenzen"


        }
        widgets = {
            "firstname": forms.TextInput(attrs={"class": "form-control", "required": "false"}),
            "lastname": forms.TextInput(attrs={"class": "form-control"}),
            "birthday": forms.DateInput(format=("%Y-%m-%d"), attrs={"class": "form-control", "placeholder": "Wähle ein Datum", "type":"date"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "adress": forms.Textarea(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control", "type": "email"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "entry_date": forms.DateInput(format=("%Y-%m-%d"), attrs={"class": "form-control", "placeholder": "Wähle ein Datum", "type":"date"}),
            "account_details": forms.Textarea(attrs={"class": "form-control"}),
            "legal_representative": forms.Textarea(attrs={"class": "form-control"}),
            "positions": forms.SelectMultiple(attrs={"class": "form-select"}),
            "modules": forms.SelectMultiple(attrs={"class": "form-select"}),
            "licenses": forms.SelectMultiple(attrs={"class": "form-select"}),
            "rate": forms.Select(attrs={"class": "form-select"}),
            "chronic_diseases": forms.Textarea(attrs={"class": "form-control"}),
            "permanent_medication": forms.Textarea(attrs={"class": "form-control"}),
            "publish_fotos": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }