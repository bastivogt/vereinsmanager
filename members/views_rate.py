from django.shortcuts import render

from members import helpers

# rate views
def rate_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/rate_index.html", {
        "title": "rate index"
    })