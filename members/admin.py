from django.contrib import admin


from . import models
from . import forms

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "get_age", "gender", "get_modules_str", "get_positions_str"]
    list_filter = ["modules", "positions", "rate", "licenses", "gender", "is_active", "publish_fotos"]
    search_fields = ["firstname", "lastname"]
    #form = forms.MemberForm
    fieldsets = [
        ("Person", {
            "fields": ("firstname", "lastname", "birthday", "gender", "adress", "email", "phone")
        }),
        ("Legal Representative", {
            "fields": ("legal_representative",),
            "classes": ("collapse", ),
        }),
        ("Association Data", {
            "fields": ("modules", "positions", "entry_date", "licenses", "rate" )
        }),
        ("Health", {
            "fields": ("chronic_diseases", "permanent_medication")
        }),
        ("Other", {
            "fields": ("publish_fotos", "is_active", )
        })


    ]


admin.site.register(models.Module)
admin.site.register(models.Position)
admin.site.register(models.Gender)
admin.site.register(models.License)
admin.site.register(models.Rate)
admin.site.register(models.Member, MemberAdmin)
