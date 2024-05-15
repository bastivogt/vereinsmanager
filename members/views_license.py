from django.shortcuts import render
from members import helpers

# license views
def license_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/license_index.html", {
        "title": "license index"
    })