from django.urls import path


from .views import license_views
from .views import member_views
from .views import module_views
from .views import position_views
from .views import rate_views


urlpatterns = [
    path("members-list/", member_views.index, name="member-index"),
    path("member/<int:id>", member_views.member_detail, name="members-member-detail"),
    path("member/new", member_views.member_new, name="members-member-new"),
    path("member/update/<int:id>", member_views.member_update, name="members-member-update"),
    path("member/delete/<int:id>", member_views.member_delete, name="members-member-delete"),

    path("modules/", module_views.module_index, name="members-module-index"),
    path("module/<int:id>", module_views.module_detail, name="members-module-detail"),
    path("module/update/<int:id>", module_views.module_update, name="members-module-update"),
    path("modules/new", module_views.module_new, name="members-module-new"),
    path("module/delete/<int:id>", module_views.module_delete, name="members-module-delete"),

    path("positions/", position_views.position_index, name="members-position-index"),

    path("rates/", rate_views.rate_index, name="members-rate-index"),

    path("licenses/", license_views.license_index, name="members-license-index")
]