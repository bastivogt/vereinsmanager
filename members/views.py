from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.db.models import Q

from . import helpers
from . import models
from . import forms



# Create your views here.

# members views
def index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    

    filter_gender = request.GET.get("gender")
    filter_module = request.GET.get("module")
    filter_position = request.GET.get("position")
    filter_publish_fotos = request.GET.get("publish_fotos")

    search = request.GET.get("search")

    print(f"search: {search}")


    default_filter_values = {
        "gender": {
            "value": "all",
            "title": "Alle"
        },
        "module": {
            "value": "all",
            "title": "Alle"
        },
        "position": {
            "value": "all",
            "title": "Alle"
        },
        "publish_fotos": {
            "value": False
        },
        "search": {
            "value": ""
        }

    }

     
    members = models.Member.objects.filter(is_active=True)
    genders = models.Gender.objects.all()
    modules = models.Module.objects.all()
    positions = models.Position.objects.all()

    if filter_gender != None and filter_gender != "all":
        members = members.filter(gender__id=int(filter_gender))
        default_filter_values["gender"]["value"] = int(filter_gender)
        default_filter_values["gender"]["title"] = genders.get(id=int(filter_gender)).name
        
    if filter_module != None and filter_module != "all":
        members = members.filter(modules__id=int(filter_module))
        default_filter_values["module"]["value"] = int(filter_module)
        default_filter_values["module"]["title"] = modules.get(id=int(filter_module)).name

    if filter_position != None and filter_position != "all":
        members = members.filter(positions__id=int(filter_position))
        default_filter_values["module"]["value"] = int(filter_position)
        default_filter_values["module"]["title"] = positions.get(id=int(filter_position)).name


    if filter_publish_fotos != None:
        members = members.filter(publish_fotos=True)
        default_filter_values["publish_fotos"]["value"] = True

    if search != "" and search != None:
        members = members.filter(Q(firstname__icontains=search) | Q(lastname__icontains=search)).distinct()
        default_filter_values["search"]["value"] = search

    print(default_filter_values)

    return render(request, "members/index.html", {
        "title": "Mitglieder Liste", 
        "members": members, 
        "genders": genders,
        "modules": modules,
        "positions": positions,
        "filter_defaults": default_filter_values
    })


# member_detail
def member_detail(request, id):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    member = get_object_or_404(models.Member, id=id)
    return render(request, "members/member_detail.html", {
        "title": "Mitglied Detail",
        "id": id,
        "member": member
    })



# module views
def module_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/module_index.html", {
        "title": "module index"
    })


# position views
def position_index(request):
    if not request.user.is_authenticated:
        return helpers.not_auth_redirect()
    
    return render(request, "members/position_index.html", {
        "title": "positions index"
    })