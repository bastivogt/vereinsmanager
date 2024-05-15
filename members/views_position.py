from django.shortcuts import render
from members import helpers

# position views
def position_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/position_index.html", {
        "title": "positions index"
    })