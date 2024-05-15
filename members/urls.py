from django.urls import path

from . import views
from . import views_rate
from . import views_license
from . import views_position
from . import views_module
from . import views_member


urlpatterns = [
    path("members-list/", views_member.index, name="members-index"),
    path("member/<int:id>", views_member.member_detail, name="members-member-detail"),
    path("member/new", views_member.member_new, name="members-member-new"),
    path("member/update/<int:id>", views_member.member_update, name="members-member-update"),
    path("member/delete/<int:id>", views_member.member_delete, name="members-member-delete"),
    path("modules/", views_module.module_index, name="members-modules-index"),
    path("positions/", views_position.position_index, name="members-positions-index"),
    path("rates/", views_rate.rate_index, name="members-rates-index"),
    path("licenses/", views_license.license_index, name="members-licenses-index")
]