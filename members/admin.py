from django.contrib import admin


from . import models

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "get_age", "gender", "get_modules_str", "get_positions_str"]
    list_filter = ["modules", "positions", "gender", "is_active", "publish_fotos"]
    search_fields = ["firstname", "lastname"]
    fieldsets = [
        ("Person", {
            "fields": ("firstname", "lastname", "birthday", "gender", "adress", "email", "phone")
        }),
        ("Legal Representative", {
            "fields": ("legal_representative",),
            "classes": ("collapse", ),
        }),
        ("Association Data", {
            "fields": ("modules", "positions", "entry_date", )
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
admin.site.register(models.Member, MemberAdmin)
