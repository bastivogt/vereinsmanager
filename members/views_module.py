from django.shortcuts import render
from members import helpers

# module views
def module_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/module_index.html", {
        "title": "module index"
    })