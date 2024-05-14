from django.urls import path

from . import views

urlpatterns = [
    path("members-list/", views.index, name="members-index"),
    path("member/<int:id>", views.member_detail, name="members-member-detail"),
    path("member/new", views.member_new, name="members-member-new"),
    path("member/update/<int:id>", views.member_update, name="members-member-update"),
    path("member/delete/<int:id>", views.member_delete, name="members-member-delete"),
    path("modules/", views.module_index, name="members-modules-index"),
    path("positions/", views.position_index, name="members-positions-index")
]