from django.urls import path

from . import views

urlpatterns = [
    path("members-list/", views.index, name="members-index"),
    path("member/<int:id>", views.member_detail, name="members-member-detail"),
    path("modules/", views.module_index, name="members-modules-index"),
    path("positions/", views.position_index, name="members-positions-index")
]